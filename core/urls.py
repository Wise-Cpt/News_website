from django.urls import path
from django.conf.urls.static import static
from config import settings
from .views import (
    ArticleDetailView, 
    IndexView, 
    ContactView,
    articles_view,
    SearchView, 
    RecruitingView,
    AboutView,
    )

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/', articles_view, name='articles'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='articledetail'),
    path('contact', ContactView.as_view(), name='contact'),
    path('about', AboutView.as_view(), name='about'),
    path('recruiting', RecruitingView.as_view(), name='recruiting'),
    path('articles/search', SearchView.as_view(), name='search'),


]



