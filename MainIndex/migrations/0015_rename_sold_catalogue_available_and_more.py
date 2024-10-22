# Generated by Django 4.0.6 on 2022-10-17 18:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0014_catalogue_geo_position_catalogue_item_tags_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogue',
            old_name='sold',
            new_name='available',
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 17, 18, 0, 40, 410863, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 17, 18, 0, 40, 376290, tzinfo=utc), null=True),
        ),
    ]
