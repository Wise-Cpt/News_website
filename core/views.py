from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView, 
)
from .models import Article, Category, Image
from .forms import CategoryCreateForm, ImageCreateForm, ArticleCreateForm

# Create your views here.

class ArticleListView(ListView):
    template_name = "index.html"
    paginate_by = 2
    model = Article
    # queryset= Article.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context["articles"] = Article.objects.all().order_by('-updated')
        context["images"] = Image.objects.all()
        context["categories"] = Category.objects.all()
        # context["test_page"] = page_obj

        return context



class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["articles"] = Article.objects.all()

        return context

# class articlelistView(ArticleListView):
#     template_name = "index2.html"
#     paginate_by = 1

#     pass

# class article2detailView(ArticleListView):
#     template_name = "article_detail.html"
#     paginate_by = 1

#     pass
