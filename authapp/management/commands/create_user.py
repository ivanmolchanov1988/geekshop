#пример для планировщика (использовать через cron в linux)

from django.core.management.base import BaseCommand, CommandError
from authapp.models import User


class Comand(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handler(self, *args, **options):
        new_user = User(email='____@__.__,', is_active=True)
        new_user.save()
        print('user created')