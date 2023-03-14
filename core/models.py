from django.db import models
from tinymce import models as tinymce_models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from account.models import Profile 
from django.contrib.auth.models import User

# Create your models here.

class AbstractSEO(models.Model):
    meta_title       = models.CharField(max_length=70, verbose_name="titre meta", blank=True, null=True)
    meta_description = models.TextField(verbose_name="description meta", blank=True, null=True)
    meta_keyword     = models.CharField(max_length=150, verbose_name="Keywords meta", blank=True, null=True)  
    class Meta:
        abstract =True

class Issue(AbstractSEO,models.Model):
    title              = models.CharField(max_length=254, verbose_name="Titre du Numéro")
    slug               = models.SlugField()
    actif              = models.BooleanField(verbose_name='actif', default=True)
    cover_a            = models.ImageField(verbose_name="image de la couverture side A", blank=True, null=True)
    cover_b            = models.ImageField(verbose_name="image de la couverture side B", blank=True, null=True)
    pdf                = models.FileField(upload_to='media', verbose_name='pdf of the issue', null=True, blank=True)
    start_date         = models.DateTimeField(verbose_name='Date debut ',  auto_now_add=True)
    end_date           = models.DateTimeField(verbose_name='Date fin',  auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:issuedetail', kwargs={'pk': self.pk})

class Category(AbstractSEO, MPTTModel):
    name  = models.CharField( max_length=150, verbose_name='Nom')
    slug  = models.SlugField( max_length=150, unique= True, verbose_name='URL')
    order  = models.IntegerField(verbose_name='ordre', null=True, blank=True)
    actif = models.BooleanField(verbose_name='actif', default=True)
    to_home_page = models.BooleanField(verbose_name="ajouter a la page d'accueil", default=False)
    to_footer = models.BooleanField(verbose_name="ajouter au footer", default=False)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created      = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        import random
        if not self.slug:
            self.slug = str(slugify(self.name) + "-" + slugify(int(random.randint(1, 10000)))
                    )
        super(Category, self).save(*args, **kwargs)  
    # def get_absolute_url(self):
    #     return reverse('core:articles', kwargs={'pk': self.pk})
    def get_absolute_url(self):
        return f"/articles/?category={self.id}"
    
    # def get_articles_of_author(self):
    #     return f"/articles/?author={self.id}"
    
    class Meta:
        verbose_name = 'Catégorie'
        verbose_name_plural = '- Catégories'
    class MPTTMeta:
        order_insertion_by = ["name"]

class Contact(models.Model):
    name        = models.CharField(verbose_name=_('Nom complet'), max_length=100)
    phone       = models.CharField(verbose_name=_("Téléphone") , max_length=25)
    email       = models.EmailField(verbose_name=_("Email"), null=True, blank =True)
    subject     = models.CharField(verbose_name=_("Sujet"), max_length=50, blank=True,null=True)
    message     = models.TextField(verbose_name=_("Message"), blank=True, null=True)
    date_sent   = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id',)
        verbose_name = 'Formulaire de contact'
        verbose_name_plural = 'Formulaire de contact'

class Hiring(models.Model):
    name        = models.CharField(max_length=150, verbose_name='Nom')
    email       = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    phone       = models.CharField(verbose_name="Téléphone" , max_length=25)
    birth_date  = models.DateField(verbose_name='date de naissance',null=True, blank=True) 
    birth_place = models.CharField(max_length=150, verbose_name='lieu de naissance', null=True, blank=True)
    message     = models.TextField(verbose_name='experience', null=True, blank=True)
    cv_file     = models.FileField(upload_to='media', verbose_name='CV', null=True, blank=True)

    class Meta:
        verbose_name = _("Recrutement")
        verbose_name_plural = _("Recrutement")
    
    def __str__(self):
        return str(self.email)
  

class Article(AbstractSEO, models.Model):
    title         = models.CharField( max_length=150, verbose_name='Titre')
    slug          = models.SlugField()
    apercu        = models.CharField( max_length=300, verbose_name='apercu', blank=True, null=True)
    chapo         = models.CharField( max_length=300, verbose_name='chapô ',blank=True, null=True)
    quote         = models.CharField( max_length=300, verbose_name='phrase mise en avant ', blank=True, null=True)
    texte_top     = tinymce_models.HTMLField(verbose_name='texte haut', blank=True, null=True)
    texte_image  = tinymce_models.HTMLField(verbose_name='texte deux colonnes', blank=True, null=True)
    texte_bottom  = tinymce_models.HTMLField(verbose_name='texte bas', blank=True, null=True)
    authors       = models.ManyToManyField(Profile, verbose_name="Auteur", related_name="articles_of_authors", blank=True)
    category      = models.ForeignKey(Category,on_delete=models.CASCADE,  verbose_name="categorie de l'article", related_name="category_of_article")
    issue         = models.ForeignKey(Issue,on_delete=models.CASCADE,   related_name="issue_of_article", blank=True, null=True)
    publish       = models.BooleanField(default=True, verbose_name='Publier',)
    en_avant = models.BooleanField(verbose_name="mettre en avant a la page d'accueil", default=False)
    to_home_page = models.BooleanField(verbose_name="ajouter a la page d'accueil", default=False)
    actif         = models.BooleanField(default=True)
    date       = models.DateTimeField(verbose_name='Date de publication', blank=True, null=True  )
    created       = models.DateTimeField(verbose_name='Date de Création',  auto_now_add=True)
    updated       = models.DateTimeField(verbose_name='Date de dernière mise à jour',  auto_now=True)
    def __str__(self):
        return str(self.title)
    def get_absolute_url(self):
        return reverse("core:articledetail", kwargs={"slug": self.slug})

 
    @property
    def first_image(self):
        image = None
        try:
            image = self.photos.first().image.url
        except:
            pass
        return image

    @property
    def last_image(self):
        image = None
        try:
            if self.photos.count() > 1:
                image = self.photos.last().image.url
        except:
            pass
        return image

    @property
    def get_authors(self):
        return ",".join([author.username for author in self.authors.all()])
        
    # @property
    # def get_articles_of_author(self):
    #     return [print(article) for article in self.article.authors]

class ArticleImage(models.Model):
    article             = models.ForeignKey(Article, related_name="photos", on_delete=models.CASCADE, null=True, blank = True)
    title               = models.CharField(max_length=254,verbose_name="Titre de l'image'")
    image               = models.ImageField(verbose_name="lmage de l'article", blank=True, null=True)
    side                = models.BooleanField(verbose_name='side picture ', default=False)
    description         = models.TextField(blank=True, null=True)
    actif               = models.BooleanField(verbose_name='actif', default=True)
    card                = models.BooleanField(verbose_name="Card image ", default=True)
    banner              = models.BooleanField(verbose_name="Banner lmage", default=True)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title
