# Generated by Django 4.0.6 on 2022-10-02 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0008_alter_users_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 10, 2, 20, 12, 46, 88399), null=True),
        ),
    ]