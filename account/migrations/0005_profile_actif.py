# Generated by Django 3.2.16 on 2023-02-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='actif',
            field=models.BooleanField(default=True, verbose_name='actif'),
        ),
    ]
