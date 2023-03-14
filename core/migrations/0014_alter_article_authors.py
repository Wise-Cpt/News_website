# Generated by Django 3.2.16 on 2023-02-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_delete_user'),
        ('core', '0013_rename_author_article_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='autors', to='account.Profile', verbose_name='Auteur'),
        ),
    ]