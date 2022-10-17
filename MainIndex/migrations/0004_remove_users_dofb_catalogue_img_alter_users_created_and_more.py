# Generated by Django 4.1.1 on 2022-09-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainIndex', '0003_catalogue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='dofb',
        ),
        migrations.AddField(
            model_name='catalogue',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]