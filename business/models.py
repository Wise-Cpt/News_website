from django.db import models
from tinymce import models as tinymce_models
from django.db.models.signals import pre_init
from solo.models import SingletonModel
from markdownx.models import MarkdownxField
from core.models import AbstractSEO
from django.core.exceptions import ValidationError
# Create your models here.


POSITION_CHOICES = [
        ('ST', 'Slider Top - Home page 1900 / 930 px (texte au centre)'),
        ('BB', 'Banner Bas - Home page 1900 / 930 px text manuel'),
        ('PP', 'Banner Pop up'),
        ('DB', 'Dual Banner'),
        ('TR', 'trio carousel'),
        ('MV', 'Mosaique verticale'),
        ('CT', 'Call to Action Top'),
        ('CA', 'Call to Action '),
        ('GB', 'gift box '),
        ('CL', 'large bottom '),
    ]


class ActiveManager(models.Manager):
    def active(self):
        return self.filter(active=True)


class MediaManager(models.Manager):
    def slider(self):
        return self.filter(actif=True, position="ST")
    def slider_mobile(self):
        return self.filter(actif=True, position="ST")
    def popup(self):
        return self.filter(actif=True, position="PP").last()
    def bottom(self):
        return self.filter(actif=True, position="BB").last()
    # def mosaic_vertical(self):
    #     return self.filter(actif=True, position="MV").last()
    # def mosaic_horizontal(self):
    #     return self.filter(actif=True, position="MH")
    # def mosaic_square(self):
    #     return self.filter(actif=True, position="MC")
    def dual_banner(self):
        return self.filter(actif=True, position="DB")[:2]
    def sub_dual_banner(self):
        return self.filter(actif=True, position="TR")
    def mosaique_banners(self):
        return self.filter(actif=True, position="MV")
    def cta_banner_top(self):
        return self.filter(actif=True, position="CT").last()
    def cta_banner(self):
        return self.filter(actif=True, position="CA").last()
    def gift_box(self):
        return self.filter(actif=True, position="GB").last()
    def cta_large_banner(self):
        return self.filter(actif=True, position="CL").last()

class Business(AbstractSEO,SingletonModel):
    name            = models.CharField(verbose_name="Nom de l'entreprise", max_length=100)
    logo            = models.ImageField(upload_to='images/logos', verbose_name='Logo')
    favicon         = models.ImageField(upload_to='images/logos', verbose_name="Favicon", blank=True, null=True)
    logo_negatif    = models.ImageField(upload_to='images/slides', verbose_name="Logo négatif", blank=True, null=True)
    popup_image     = models.ImageField(upload_to='images/slides', verbose_name="image sur popup homepage", blank=True, null=True)
    title           = models.CharField(verbose_name="Titre", max_length=50, blank=True)
    address         = models.CharField(verbose_name="Adresse", max_length=50, blank=True)
    email           = models.EmailField(verbose_name="email de l'entreprise", max_length=50, blank=True)
    email2          = models.EmailField(verbose_name="2eme email de l'entreprise", max_length=50, blank=True)
    phone           = models.CharField(verbose_name="numéro de téléphone de l'entreprise", max_length=50, blank=True)
    phone2          = models.CharField(verbose_name="2eme numéro de téléphone de l'entreprise", max_length=50, null=True,blank=True)
    phone3          = models.CharField(verbose_name="3eme numéro de téléphone de l'entreprise", max_length=50, null=True,blank=True)
    postal_code     = models.DecimalField(verbose_name="code postal ",max_digits=7,decimal_places=0, blank=True, null=True)
    about           = tinymce_models.HTMLField(verbose_name='Text a propos', blank=True, null=True)
    mini_about      = models.TextField(verbose_name="Petit texte a propos de l'entreprise ( bas de page)", blank=True, null=True)
    about_photo     = models.ImageField(verbose_name="Photo A propos 440 X 275 px", upload_to='slides/', blank=True, null=True)
    facebook        = models.URLField(verbose_name="Lien page Facebook", max_length=300, blank=True, null=True)
    insta           = models.URLField(verbose_name="Lien page Instagram", max_length=300, blank=True, null=True)
    twitter         = models.URLField(verbose_name="Lien Compte Twitter", max_length=300, blank=True, null=True)
    linkedin        = models.URLField(verbose_name="Lien Compte linkedin", max_length=300, blank=True, null=True)
    pinterest       = models.URLField(verbose_name="Lien Compte pinterest", max_length=300, blank=True, null=True)
    snapchat        = models.URLField(verbose_name="Lien Compte snapchat ", max_length=300, blank=True, null=True)
    tiktok          = models.URLField(verbose_name="Lien Compte tiktok", max_length=300, blank=True, null=True)
    google_plus     = models.URLField(verbose_name="Lien Compte Google plus", max_length=300, blank=True, null=True)
    youtube         = models.URLField(verbose_name="Lien Chaine Youtube", max_length=300, blank=True, null=True)
    tag_header      = MarkdownxField(verbose_name='Google tag manager header', blank=True, null=True)
    tag_body        = MarkdownxField(verbose_name='Google tag manager body', blank=True, null=True)
    chat_code       = MarkdownxField(verbose_name="Script messagerie instantané", blank=True, null=True)
    pixel           = MarkdownxField(verbose_name="Script Facebook pixel", blank=True, null=True)
    analytics       = MarkdownxField(verbose_name="Script Analytics", blank=True, null=True)
    contact_message = MarkdownxField(verbose_name="Contact message", blank=True, null=True)
    google_maps     = MarkdownxField(verbose_name="iframe google maps", blank=True, null=True)
    messenger_script = MarkdownxField(blank=True, null=True)
    class Meta:
        verbose_name = '1. Infomation'
        verbose_name = '1. Infomations'

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError("Vous ne pouvez pas rajouter d'entreprise")

class Slide(models.Model):
    photo      = models.ImageField(verbose_name="Media fichier", upload_to='slides/' )
    photo_mobile      = models.ImageField(verbose_name="Media fichier mobile", upload_to='slides/', blank=True, null=True )
    position   = models.CharField(choices=POSITION_CHOICES, verbose_name="Placement", max_length=50, blank=True, null=True) 
    order  = models.IntegerField(verbose_name='ordre', null=True, blank=True)
    title      = models.CharField(verbose_name="Grand titre de la photo", max_length=50, blank=True, null=True) 
    sub_title  = models.CharField(verbose_name="Sous titre de la photo", max_length=50, blank=True, null=True) 
    url        = models.URLField(verbose_name="Lien", max_length=250, blank=True, null=True)
    actif  = models.BooleanField(verbose_name='actif', default=True)
    objects = ActiveManager()
    place = MediaManager()

    class Meta:
        verbose_name = ' Media'
        verbose_name_plural = ' Medias'
