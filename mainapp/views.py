from django.shortcuts import render
import json

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    with open(
            'mainapp/templates/mainapp/fixtures/products.json', 'r', encoding='utf-8') as oJson:
        loadJson = json.load(oJson)
    context = {
        'menu': [
            {'name': 'Новинки'},
            {'name': 'Одежда'},
            {'name': 'Обувь'},
            {'name': 'Аксессуары'},
            {'name': 'Подарки'},
        ],
        'products': loadJson
    }
    return render(request, 'mainapp/products.html', context)


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