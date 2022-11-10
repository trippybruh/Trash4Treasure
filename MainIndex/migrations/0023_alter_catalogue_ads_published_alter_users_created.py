# Generated by Django 4.0.6 on 2022-10-26 08:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0022_users_country_alter_catalogue_ads_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 8, 56, 40, 505568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 8, 56, 40, 414746, tzinfo=utc)),
        ),
    ]
