from django.db import models
from django.conf import settings
# Create your models here.

class Role(models.Model):
    name    = models.CharField(max_length=30, verbose_name="role")
    active  = models.BooleanField(default=True, verbose_name="Livraison Active")
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"        
    def __str__(self):
        return self.name 

class Profile(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    picture     = models.ImageField(upload_to='images/faces', null=True, blank=True)
    username    = models.CharField(max_length=20 , null=True, blank=True)
    phone       = models.CharField(max_length=20 , blank=True)
    address     = models.CharField(max_length=250 , blank=True)
    role        = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        # return f'{self.username}'
        return str(self.username)


 