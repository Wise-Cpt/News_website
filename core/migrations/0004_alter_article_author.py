# Generated by Django 3.2.16 on 2023-01-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('core', '0003_article_to_home_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='autors', to='account.Profile', verbose_name='Auteur'),
        ),
    ]