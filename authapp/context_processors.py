from basket.models import Basket

#def user_status(request):
def user_counter(request):
    user = request.user
    if user.is_authenticated:
        counter = Basket.objects.filter(user=user).count()
    else:
        counter = 0

    return {'user_counter': counter}