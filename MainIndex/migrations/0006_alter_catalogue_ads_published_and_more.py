# Generated by Django 4.1.1 on 2022-10-02 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0005_users_id_alter_catalogue_nickname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogue',
            name='ads_published',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='catalogue',
            name='ads_removed',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateField(),
        ),
    ]