from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth, messages
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from authapp.forms import UserLoginForm, UserRegisterform, UserProfileForm, ShopUserProfileEditForm
from basket.models import Basket
#from authapp.models import User

from django.http import HttpResponse
from authapp.models import User
from authapp.utils import send_verify_email

# Create your views here.

def verify(request, user_id, hash):
    #return HttpResponse(f'{user_id} {hash}')
    #user = User.objects.get(pk=user_id)
    user = get_object_or_404(User, pk=user_id)
    if user.activation_key == hash and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = None
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'authapp/verification.html')
    else:
        return HttpResponseRedirect(reverse('authapp:login'))
    #
    #return HttpResponse(f'{user_id} {hash}')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print('!!!', form.errors)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterform(data=request.POST)
        if form.is_valid():
            #form.save()
            user = form.save()
            send_verify_email(user)
            #messages.success(request, 'Вы успешно зарегистрировались!')
            messages.success(request, 'Пройдите по ссылке для регистрации')
            return HttpResponseRedirect(reverse('authapp:login'))
        # else:
        #     print(form.errors)
    else:
        form = UserRegisterform()
    context = {'form': form}
    return render(request, 'authapp/register.html', context)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(data=request.POST, instance=request.user.shopuserprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('authapp:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    # total_quantity = 0
    # total_sum = 0
    # baskets = Basket.objects.filter(user=request.user)
    #
    # for basket in baskets:
    #     total_quantity += basket.quatity
    #     total_sum += basket.sum()

    baskets = Basket.objects.filter(user=request.user)

    context = {'form': form,
               'profile_form': profile_form,
               'baskets': baskets,
               }
    return render(request, 'authapp/profile.html', context)