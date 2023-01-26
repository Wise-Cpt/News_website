from django.contrib import admin
from django.utils.html import format_html
from .models import Article, Category, ArticleImage, Contact, Hiring, Issue
# Register your models here.

class ArticleImageLinesAdmin(admin.TabularInline):
    def image_tag(self):
        return format_html('<img src="{}" height="150" />'.format(self.fichier.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    model = ArticleImage
    readonly_fields= (image_tag,)
    extra = 1

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id','title')
    list_per_page = 40

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'actif','to_home_page', 'to_footer')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 50
    list_editable = [ 'actif', 'to_home_page', 'to_footer']
    search_fields = ('name',)

class ArticleAdmin( admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'publish', 'created',)
    prepopulated_fields = {"slug": ("title",)}
    list_display_links = ('id','title' , )
    list_per_page = 40
    save_as = True
    list_filter = ( 'title', 'category','author', 'publish', 'created','updated' )
    list_editable = [ 'category','publish',]
    search_fields = ('title', 'category','author', 'publish',)
    inlines = [ArticleImageLinesAdmin,]

class ContactAdmin(admin.ModelAdmin):     
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_per_page = 40
    list_filter = ('name', 'phone', 'email',)
    search_fields = ('id', 'phone', 'email')
    readonly_fields = ('date_sent',)

class IssueAdmin( admin.ModelAdmin):
    list_display = ('id', 'title', 'actif', 'start_date', 'end_date',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Issue, IssueAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(ArticleImage,ImageAdmin)
admin.site.register(Contact, ContactAdmin) 
admin.site.register(Hiring) 
