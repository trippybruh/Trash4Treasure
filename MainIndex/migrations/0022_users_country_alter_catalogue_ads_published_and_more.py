# Generated by Django 4.0.6 on 2022-10-23 16:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0021_alter_catalogue_ads_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='country',
            field=models.CharField(default='Italy', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 16, 53, 56, 500637, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='region',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 16, 53, 56, 469638, tzinfo=utc)),
        ),
    ]
