# Generated by Django 3.1.7 on 2021-03-19 14:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210318_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 21, 14, 58, 55, 479943, tzinfo=utc)),
        ),
    ]
