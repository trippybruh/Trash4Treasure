# Generated by Django 4.0.6 on 2022-10-23 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0020_alter_catalogue_options_alter_users_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 16, 46, 2, 924245, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='geo_position',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='item_tags',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 16, 46, 2, 892057, tzinfo=utc)),
        ),
    ]
