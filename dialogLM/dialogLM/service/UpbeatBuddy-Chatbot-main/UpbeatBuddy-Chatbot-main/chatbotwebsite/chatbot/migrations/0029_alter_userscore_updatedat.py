# Generated by Django 3.2.13 on 2024-01-27 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0028_auto_20240127_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscore',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 21, 16, 0, 166400)),
        ),
    ]