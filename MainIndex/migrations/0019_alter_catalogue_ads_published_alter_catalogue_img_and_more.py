# Generated by Django 4.0.6 on 2022-10-19 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0018_alter_catalogue_ads_published_alter_catalogue_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 15, 53, 37, 727198, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='img',
            field=models.ImageField(default='static/logos/trashbin.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 19, 15, 53, 37, 687198, tzinfo=utc)),
        ),
    ]