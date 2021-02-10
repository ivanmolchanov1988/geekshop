from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from authapp.forms import UserLoginForm, UserRegisterform, UserProfileForm
from basket.models import Basket
#from authapp.models import User

# Create your views here.

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
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            print(form.errors)
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
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    # total_quantity = 0
    # total_sum = 0
    # baskets = Basket.objects.filter(user=request.user)
    #
    # for basket in baskets:
    #     total_quantity += basket.quatity
    #     total_sum += basket.sum()

    baskets = Basket.objects.filter(user=request.user)

    context = {'form': form,
               'baskets': baskets,
               }
    return render(request, 'authapp/profile.html', context)