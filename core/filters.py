from .models import Article, Category
import django_filters

def is_valid_queryparam(param):
    if param != '' and param != None:
        print('THE PARA1M', param)
        return True

def get_filtered_articles(request):
    context = {}
    category_id = request.GET.get('category')
    author_id = request.GET.get('author')

    qs = Article.objects.filter(publish=True)
    # dictio = []
    context["article_categories"] = Category.objects.filter( actif=True)

    if is_valid_queryparam(category_id):
        cat = Category.objects.get(id=category_id)
        context["selected_category"] = cat
        # print("This is the result of the query: ---> ",context["selected_category"] )
        # context["article_categories"] = Article.objects.get(id = category_id)
        # print("This is the result of the query: ---> ",context["article_categories"] )

        children = cat.get_children()
        qs = qs.filter(category__in=cat.get_descendants(include_self=True), actif=True)
        if children.count():
            context["article_categories"] = children
        else : 
            context["article_categories"] =  cat.get_siblings(include_self=True)
    return {'qs': qs.distinct(), 'context': context}



# class ArticleFilter(django_filters.FilterSet):
#     author = django_filters.CharFilter(lookup_expr='iexact')
#     category = django_filters.CharFilter(lookup_expr='iexact')

#     class Meta:
#         model = Article
#         fields = ['authors', 'category']

