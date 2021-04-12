from django.test import TestCase
from django.test.client import Client
from authapp.models import User
from django.core.management import call_command

# Create your tests here.

class TestUserManagement(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

        self.superuser = User.objects.create_superuser('django2', 'django@yandex.ru', '1349')
        self.user = User.objects.create_user('tarantino', 'tarantino@yandex.ru', '1349')
        self.user_with__first_name = User.objects.create_user('turman', 'turman@yandex.ru', '1349',
                                                              first_name='Ума')

    def test_user_login(self):
        # главная без логина
        resource = self.client.get('/')
        self.assertEqual(resource.status_code, 200)
        self.assertTrue(resource.context['user'].is_anonymous)
        #self.assertEqual(resource.context['title'], 'Главная')
        self.assertNotContains(resource, 'Пользователь', status_code=200)

        # данные пользователя
        self.client.login(username='tarantino', password='1349')

        # логинимся
        resource = self.client.get('/auth/login/')
        self.assertFalse(resource.context['user'].is_anonymous)
        self.assertEqual(resource.context['user'], self.user)

        # главная после логина
        resource = self.client.get('/')
        #self.assertContains(resource, 'Пользователь', status_code=200)
        self.assertEqual(resource.context['user'], self.user)
        # self.assertIn('Пользователь', resource.content.decode())

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basket')
