from django.contrib import admin
from .models import Profile, Role


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'username' , 'phone' , 'address', 'picture', 'actif', ]

admin.site.register(Role) 
