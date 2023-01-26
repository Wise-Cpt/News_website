# Generated by Django 3.2.16 on 2023-01-23 15:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_alter_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleimage',
            old_name='produit',
            new_name='article',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(blank=True, related_name='autors', to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
    ]