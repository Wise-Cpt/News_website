from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView, 
    TemplateView,
    CreateView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from business.models import Slide
from .models import Article,Category, Contact
from .forms import  ContactForm
from .filters import get_filtered_articles
# Create your views here.

########## HOMEPAGE ##########
class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"]           = Slide.place.slider()
        context["homepage_articles"]            = Article.objects.filter(en_avant=True)
        context["homepage_article_list"]          = Article.objects.filter(to_home_page=True)
        context["homepage_card_articles"]          = Article.objects.filter(to_home_page=True)
        return context

########## ARTICLE ##########
#### LIST 
def articles_view(request):
    filtered_products= get_filtered_articles(request)
    context = filtered_products['context']
    queryset = filtered_products['qs']
    context['articles'] = queryset
    #start paginate
    paginator = Paginator(queryset, 21)
    page = request.GET.get('page')
    get_copy = request.GET.copy()
    try:
        context['articles'] = paginator.page(page)
    except PageNotAnInteger:
        context['articles'] = paginator.page(1)
    except EmptyPage:
        context['articles'] = paginator.page(paginator.num_pages)
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    context['parameters'] = parameters
    return render(request, 'articles.html', context)
#### DETAIL
class ArticleDetailView(DetailView):
    template_name = "article_detail.html"
    model = Article 
    def get_context_data(self,  *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args,**kwargs)
        article = self.get_object()
        category = article.category
        articles =  Article.objects.filter(category=category, publish=True)
        context["related_articles"] = articles.exclude(id= article.id).order_by('?')[:8]
        context["categories"] = Category.objects.all()
        return context

########## CONTACT ##########
class ContactView(SuccessMessageMixin, CreateView):
    template_name= "contact.html"
    form_class= ContactForm
    model = Contact 
    success_message = "تم استلام رسالتك ، شكرا لك"
    success_url = reverse_lazy('core:contact')
    def form_valid(self, form):
        try: 
            form.send_email() 
        except: 
            pass
        return super().form_valid(form)