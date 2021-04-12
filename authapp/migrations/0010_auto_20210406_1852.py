# Generated by Django 3.1.7 on 2021-04-06 15:52

import authapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_auto_20210402_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=authapp.models.default_expire_time),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default=18, null=True),
        ),
    ]