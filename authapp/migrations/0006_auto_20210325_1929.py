# Generated by Django 3.1.7 on 2021-03-25 16:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_auto_20210319_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 16, 29, 17, 449233, tzinfo=utc)),
        ),
    ]
