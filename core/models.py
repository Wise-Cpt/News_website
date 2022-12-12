from django.db import models
from tinymce import models as tinymce_models
from django.urls import reverse


# Create your models here.

class Image(models.Model):
    title               = models.CharField(max_length=254,verbose_name="Titre de l'image'")
    image               = models.ImageField(verbose_name="l'image de l'article", blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name                = models.CharField(max_length=254, verbose_name="Nom de la categorie")
    description         = models.TextField(blank=True, null=True)
    parent              = models.ForeignKey("self",on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    


class Article(models.Model):
    title               = models.CharField(max_length=254, verbose_name="Titre de l'article")
    description_min     = models.TextField(blank=True, null=True)
    description_max     = tinymce_models.HTMLField(verbose_name='Description totale de l\'article', blank=True, null=True)
    actif               = models.BooleanField(default=False)
    image               = models.ForeignKey(Image,on_delete=models.CASCADE, verbose_name="L'image de l'article", related_name="image_of_article")
    category            = models.ForeignKey(Category,on_delete=models.CASCADE,  verbose_name="categorie de l'article", default="")

    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:articledetail', kwargs={'pk': self.pk})
