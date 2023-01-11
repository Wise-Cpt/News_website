from django.urls import path
from django.conf.urls.static import static
from config import settings
from .views import ArticleListView, ArticleDetailView, CategoryDetailView,IndexView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles', ArticleListView.as_view(), name='articlelist'),
    path('category-<int:pk>', CategoryDetailView.as_view(), name='categorydetail'),
    path('article-<int:pk>', ArticleDetailView.as_view(), name='articledetail'),
    # path('article-liste_2', ArticleListView.as_view(), name='articlelist'),
    # path('article-liste_2/article-<int:pk>', articledetailView.as_view(), name='article2detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

