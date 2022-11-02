# Generated by Django 4.0.6 on 2022-10-26 15:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainIndex', '0023_alter_catalogue_ads_published_alter_users_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='django_model_user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 17, 53, 25, 630244)),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 17, 53, 25, 630244)),
        ),
    ]