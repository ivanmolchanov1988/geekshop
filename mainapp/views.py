from django.shortcuts import render
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from mainapp.models import Product, ProductCategory

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


# def products(request, category_id=None):
#
#     with open(
#             'mainapp/templates/mainapp/fixtures/products.json', 'r', encoding='utf-8') as oJson:
#         loadJson = json.load(oJson)
#
#     product = None
#     if category_id:
#         #print('1')
#         pr = Product.objects.filter(category_id=category_id)
#         context = {
#             'ps': loadJson,
#             'products': pr,
#             'categories': ProductCategory.objects.all(),
#         }
#     else:
#         #print('2')
#         context = {
#             # если я комментирую кусок кода (список menu, к примеру),
#             # то у меня отваливаются продукты (с категориями всё нормально)
#             # я не понимаю в чём проблема. Потратил на это 2 часа :/
#             # я не хочу ничего удалять, но и закомментировать не могу, оставляю как есть.
#             'menu': [
#                 {'name': 'Новинки'},
#                 {'name': 'Одежда'},
#                 {'name': 'Обувь'},
#                 {'name': 'Аксессуары'},
#                 {'name': 'Подарки'},
#             ],
#             'ps': loadJson,
#             'products': Product.objects.all(),
#             'categories': ProductCategory.objects.all(),
#         }
#     return render(request, 'mainapp/products.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        product = Product.objects.filter(category_id=category_id).order_by('-price') # "-" -> это для сортировки в обратую сторону
    else:
        product = Product.objects.all().order_by('-price')
    paginator = Paginator(object_list=product, per_page=1)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'categories': ProductCategory.get_all(),
        'products': products_paginator,
    }

    return render(request, 'mainapp/products.html', context)

# оставлю для тестов
def test_context(request):
    context = {
        'title': 'test Context',
        'header': 'Добро пожаловать!',
        'username': 'Иван Молчанов',
        'products': [
            {'name': 'Худи черного цвета', 'prise': '6 009,00'},
            {'name': 'Куртка черного цвета', 'prise': '7 009,00'},
            {'name': 'Штаны черного цвета', 'prise': '8 009,00'},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Рюкзак черного цвета', 'prise': '5 009,00'},
            {'name': 'Тапки черного цвета', 'prise': '3 009,00'},
        ],
    }
    return render(request, 'mainapp/context.html', context)