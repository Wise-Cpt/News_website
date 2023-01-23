# Generated by Django 3.2.16 on 2023-01-23 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=70, null=True, verbose_name='titre meta')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='description meta')),
                ('meta_keyword', models.CharField(blank=True, max_length=150, null=True, verbose_name='Keywords meta')),
                ('title', models.CharField(max_length=150, verbose_name='Titre')),
                ('slug', models.SlugField()),
                ('aperçu', models.CharField(blank=True, max_length=300, null=True, verbose_name='aperçu')),
                ('chapo', models.CharField(blank=True, max_length=300, null=True, verbose_name='chapô ')),
                ('quote', models.CharField(blank=True, max_length=300, null=True, verbose_name='phrase mise en avant ')),
                ('texte_top', tinymce.models.HTMLField(blank=True, null=True, verbose_name='texte haut')),
                ('texte_bottom', tinymce.models.HTMLField(blank=True, null=True, verbose_name='texte bas')),
                ('publish', models.BooleanField(default=True, verbose_name='Publier')),
                ('actif', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('author', models.ManyToManyField(blank=True, related_name='autors', to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom complet')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('subject', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sujet')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Formulaire de contact',
                'verbose_name_plural': 'Formulaire de contact',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='date de naissance')),
                ('birth_place', models.CharField(blank=True, max_length=150, null=True, verbose_name='lieu de naissance')),
                ('message', models.TextField(blank=True, null=True, verbose_name='experience')),
                ('cv_file', models.FileField(blank=True, null=True, upload_to='media', verbose_name='CV')),
            ],
            options={
                'verbose_name': 'Recrutement',
                'verbose_name_plural': 'Recrutement',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=70, null=True, verbose_name='titre meta')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='description meta')),
                ('meta_keyword', models.CharField(blank=True, max_length=150, null=True, verbose_name='Keywords meta')),
                ('title', models.CharField(max_length=254, verbose_name='Nom de la categorie')),
                ('slug', models.SlugField()),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
                ('cover_a', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image de la couverture side A')),
                ('cover_b', models.ImageField(blank=True, null=True, upload_to='', verbose_name='image de la couverture side B')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media', verbose_name='pdf of the issue')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Date debut ')),
                ('end_date', models.DateTimeField(auto_now_add=True, verbose_name='Date fin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=70, null=True, verbose_name='titre meta')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='description meta')),
                ('meta_keyword', models.CharField(blank=True, max_length=150, null=True, verbose_name='Keywords meta')),
                ('name', models.CharField(max_length=150, verbose_name='Nom')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='ordre')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
                ('to_home_page', models.BooleanField(default=False, verbose_name="ajouter a la page d'accueil")),
                ('to_footer', models.BooleanField(default=False, verbose_name='ajouter au footer')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Date de dernière mise à jour')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.category')),
            ],
            options={
                'verbose_name': 'Catégorie',
                'verbose_name_plural': '- Catégories',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, verbose_name="Titre de l'image'")),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name="lmage de l'article")),
                ('description', models.TextField(blank=True, null=True)),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
                ('card', models.BooleanField(default=True, verbose_name='Card image ')),
                ('banner', models.BooleanField(default=True, verbose_name='Banner lmage')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('produit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='core.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_of_article', to='core.category', verbose_name="categorie de l'article"),
        ),
        migrations.AddField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_of_article', to='core.issue'),
        ),
    ]
