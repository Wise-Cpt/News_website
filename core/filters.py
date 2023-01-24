from .models import Article, Category

def is_valid_queryparam(param):
    if param != '' and param != None:
        print('THE PARA1M', param)
        return True

def get_filtered_articles(request):
    context = {}
    qs = Article.objects.filter(publish=True)
    dictio = []
    category_id = request.GET.get('category')
    context["article_categories"] = Category.objects.filter(level=0, actif=True)

    if is_valid_queryparam(category_id):
        cat = Category.objects.get(id=category_id)
        context["selected_category"] = Category.objects.get(id=category_id)
        children = cat.get_children()
        qs = qs.filter(category__in=cat.get_descendants(include_self=True), actif=True)
        if children.count():
            context["article_categories"] = children
        else : 
            context["article_categories"] =  cat.get_siblings(include_self=True)
    return {'qs': qs.distinct(), 'context': context}