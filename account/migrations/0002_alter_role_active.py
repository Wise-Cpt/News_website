# Generated by Django 3.2.16 on 2023-01-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
