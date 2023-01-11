
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from config import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib.sitemaps.views import sitemap
# from core.sitemaps import ProductSitemap, CategorySitemap, BrandSitemap, StaticSitemap
from django.views.generic import TemplateView

# sitemaps = {
#     'products': ProductSitemap,
#     'categories': CategorySitemap,
#     'brands': BrandSitemap,
#     'static': StaticSitemap
# }
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('core.urls')),
    path('markdownx/', include('markdownx.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")), 
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=  i18n_patterns(path('admin/', admin.site.urls),)
    # urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    # urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
    # urlpatterns += path('admin/', admin.site.urls),
else:
    urlpatterns +=  i18n_patterns(
        path('admin-zone/', admin.site.urls),
        )