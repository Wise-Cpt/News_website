# Generated by Django 3.2.12 on 2023-04-06 09:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_job_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name="Nom de l'entreprise")),
                ('image_high', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image_1')),
                ('image_low', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image_2')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Titre')),
                ('about_high', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text a propos')),
                ('about_low', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Page a propos 2')),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'abouts',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='ordre'),
        ),
    ]