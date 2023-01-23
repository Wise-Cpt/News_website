# Generated by Django 3.2.16 on 2023-01-23 09:01

from django.db import migrations, models
import markdownx.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=70, null=True, verbose_name='titre meta')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='description meta')),
                ('meta_keyword', models.CharField(blank=True, max_length=150, null=True, verbose_name='Keywords meta')),
                ('name', models.CharField(max_length=100, verbose_name="Nom de l'entreprise")),
                ('logo', models.ImageField(upload_to='images/logos', verbose_name='Logo')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='images/logos', verbose_name='Favicon')),
                ('logo_negatif', models.ImageField(blank=True, null=True, upload_to='images/slides', verbose_name='Logo négatif')),
                ('popup_image', models.ImageField(blank=True, null=True, upload_to='images/slides', verbose_name='image sur popup homepage')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Titre')),
                ('address', models.CharField(blank=True, max_length=50, verbose_name='Adresse')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name="email de l'entreprise")),
                ('email2', models.EmailField(blank=True, max_length=50, verbose_name="2eme email de l'entreprise")),
                ('phone', models.CharField(blank=True, max_length=50, verbose_name="numéro de téléphone de l'entreprise")),
                ('phone2', models.CharField(blank=True, max_length=50, null=True, verbose_name="2eme numéro de téléphone de l'entreprise")),
                ('phone3', models.CharField(blank=True, max_length=50, null=True, verbose_name="3eme numéro de téléphone de l'entreprise")),
                ('postal_code', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True, verbose_name='code postal ')),
                ('about', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text a propos')),
                ('mini_about', models.TextField(blank=True, null=True, verbose_name="Petit texte a propos de l'entreprise ( bas de page)")),
                ('about_photo', models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Photo A propos 440 X 275 px')),
                ('facebook', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien page Facebook')),
                ('insta', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien page Instagram')),
                ('twitter', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte Twitter')),
                ('linkedin', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte linkedin')),
                ('pinterest', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte pinterest')),
                ('snapchat', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte snapchat ')),
                ('tiktok', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte tiktok')),
                ('google_plus', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Compte Google plus')),
                ('youtube', models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien Chaine Youtube')),
                ('tag_header', markdownx.models.MarkdownxField(blank=True, null=True, verbose_name='Google tag manager header')),
                ('tag_body', markdownx.models.MarkdownxField(blank=True, null=True, verbose_name='Google tag manager body')),
                ('chat_code', markdownx.models.MarkdownxField(blank=True, null=True, verbose_name='Script messagerie instantané')),
                ('pixel', markdownx.models.MarkdownxField(blank=True, null=True, verbose_name='Script Facebook pixel')),
                ('analytics', markdownx.models.MarkdownxField(blank=True, null=True, verbose_name='Script Analytics')),
                ('contact_message', markdownx.models.MarkdownxField(blank=True, null=True, verbose_name='Contact message')),
                ('google_maps', markdownx.models.MarkdownxField(blank=True, null=True, verbose_name='iframe google maps')),
                ('messenger_script', markdownx.models.MarkdownxField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '1. Infomations',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='slides/', verbose_name='Media fichier')),
                ('photo_mobile', models.ImageField(blank=True, null=True, upload_to='slides/', verbose_name='Media fichier mobile')),
                ('position', models.CharField(blank=True, choices=[('ST', 'Slider Top - Home page 1900 / 930 px (texte au centre)'), ('BB', 'Banner Bas - Home page 1900 / 930 px text manuel'), ('PP', 'Banner Pop up'), ('DB', 'Dual Banner'), ('TR', 'trio carousel'), ('MV', 'Mosaique verticale'), ('CT', 'Call to Action Top'), ('CA', 'Call to Action '), ('GB', 'gift box '), ('CL', 'large bottom ')], max_length=50, null=True, verbose_name='Placement')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='ordre')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Grand titre de la photo')),
                ('sub_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sous titre de la photo')),
                ('url', models.URLField(blank=True, max_length=250, null=True, verbose_name='Lien')),
                ('actif', models.BooleanField(default=True, verbose_name='actif')),
            ],
            options={
                'verbose_name': ' Media',
                'verbose_name_plural': ' Medias',
            },
        ),
    ]
