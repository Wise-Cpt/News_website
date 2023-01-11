from django.shortcuts import render
from django.core.paginator import Paginator

from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView, 
    TemplateView,
)
from .models import Article, Category, ArticleImage
from business.models import Slide
from .forms import CategoryCreateForm, ImageCreateForm, ArticleCreateForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["slider"]           = Slide.place.slider()

        return context

class ArticleListView(ListView):
    template_name = "article _ist.html"
    paginate_by = 2
    model = Article
    # queryset= Article.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context["articles"] = Article.objects.all().order_by('-updated')
        context["images"] = ArticleImage.objects.all()
        context["categories"] = Category.objects.all()
        # context["test_page"] = page_obj

        return context



class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["articles"] = Article.objects.all()
        context["categories"] = Category.objects.all()
        return context
    
    # def get_template_names(self) :
    #     cat_param = self.request.GET.get('category', None)
    #     if cat_param:
    #         return "article_detail.html"


class CategoryDetailView(ListView):
    template_name = "category_detail.html"
    model = Article
    paginate_by = 2
    def get_queryset(self):
        cat_param = self.request.GET.get('category', None)
        if cat_param:
            articles = Article.objects.filter(category=cat_param)
            return articles
        return super().get_queryset()
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        # context["articles"] = Article.objects.all().order_by('-updated')
        context["images"] = ArticleImage.objects.all()
        context["categories"] = Category.objects.all()
        cat_param = self.request.GET.get('category', None)
        if cat_param:
            context['s_cat'] = Category.objects.get(id = cat_param)

        return context

# class articlelistView(ArticleListView):
#     template_name = "index2.html"
#     paginate_by = 1

#     pass

# class article2detailView(ArticleListView):
#     template_name = "article_detail.html"
#     paginate_by = 1

#     pass
