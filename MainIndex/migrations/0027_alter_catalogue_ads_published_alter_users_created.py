# Generated by Django 4.0.6 on 2022-11-04 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0026_remove_users_wishlist_users_item1_users_item2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 18, 39, 11, 459753)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 4, 18, 39, 11, 459753)),
        ),
    ]