from django.urls import path
from django.conf.urls.static import static
from config import settings
from .views import (
    ArticleDetailView, 
    IndexView, 
    ContactView,
    articles_view,
    )

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/', articles_view, name='articles'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='articledetail'),
    path('contact', ContactView.as_view(), name='contact'),

]



