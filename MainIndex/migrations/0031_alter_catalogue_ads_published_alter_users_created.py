# Generated by Django 4.0.6 on 2022-11-07 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0030_catalogue_popularity_alter_catalogue_ads_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 22, 8, 27, 323399)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 7, 22, 8, 27, 324397)),
        ),
    ]