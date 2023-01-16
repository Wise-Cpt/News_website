from django.contrib import admin
from .models import Business, Slide
from django.utils.html import format_html
from django.utils.html import format_html
from solo.admin import SingletonModelAdmin
# Register your models here.

class BusinesAdmin(SingletonModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class SlideAdmin(admin.ModelAdmin):
    def image_tag(self):
        return format_html('<img src="{}" height="150" />'.format(self.photo.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ('id', 'actif', 'title','sub_title', 'position','photo', image_tag, 'url')
    list_display_links = ('id',image_tag )
    list_editable = ['photo', 'url', 'actif', 'title','sub_title', 'position']

admin.site.register(Business, BusinesAdmin)
admin.site.register(Slide, SlideAdmin)
