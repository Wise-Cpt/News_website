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
from django.core.paginator import Paginator
from account.models import Profile
from django.db.models import Q

# Create your views here.

########## HOMEPAGE ##########
class IndexView(ListView):
    model = Article
    template_name = "index.html"

    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sliders"]           = Slide.place.slider()
        context["homepage_articles"]            = Article.objects.filter(en_avant=True).order_by('-updated')
        context["homepage_article_list"]          = Article.objects.filter(to_home_page=True).order_by('-updated')
        context["homepage_card_articles"]          = Article.objects.filter(to_home_page=True).order_by('-updated') 
        return context

########## ARTICLE ##########

#### LIST #######
def articles_view(request):

    filtered_articles= get_filtered_articles(request)
    context = filtered_articles['context']
    queryset = filtered_articles['qs']
    articles = queryset.order_by('-updated')
    context['articles'] = articles
    context["homepage_article_list"]= Article.objects.filter(to_home_page=True).order_by('-updated')
    context["homepage_card_articles"]          = Article.objects.filter(to_home_page=True).order_by('-updated') 
    context["all_authors"] = Profile.objects.all()

    #start paginate
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    get_copy = request.GET.copy()
    #SIDOU edit page:
    # page_obj = paginator.get_page(page_number)

    # context = {'articles': page_obj, }
    # authrs = Profile.objects.all().values_list('id')
    # print("The authors: ========> ", authrs)


    try:
        context['articles'] = paginator.page(page_number)
    except PageNotAnInteger:
        context['articles'] = paginator.page(1)
    except EmptyPage:
        context['articles'] = paginator.page(paginator.num_pages)
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    context['parameters'] = parameters
    return render(request, 'articles.html', context)

######### DETAIL ##########
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
        # context["article_categories"] = get_filtered_articles
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
    

########## Search ##########

class SearchView(ListView):
    model = Article
    template_name = "search.html"
    paginate_by = 8

    def get_queryset(self):  # new
        query = self.request.GET.get("search")
        
        object_list = Article.objects.filter(
            Q(title__icontains=query) | Q(apercu__icontains=query)| Q(chapo__icontains=query)| Q(quote__icontains=query)|
            Q(category__name__icontains=query) | Q(authors__username__icontains=query) | Q(texte_image__icontains=query)
        )
        return object_list
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["homepage_articles"]            = Article.objects.filter(en_avant=True).order_by('-updated')
        context["homepage_article_list"]          = Article.objects.filter(to_home_page=True).order_by('-updated')
        context["homepage_card_articles"]          = Article.objects.filter(to_home_page=True).order_by('-updated') 
        return context