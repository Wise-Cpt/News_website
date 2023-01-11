from django.shortcuts import render , get_object_or_404
from .models import Business
from core.models import Category 
from django.db.models import F, Q

def infos(request):
    business = Business.objects.first()
    categories = Category.objects.filter(actif=True)
    footer_categories = Category.objects.filter(Q(actif=True) & Q(to_footer=True) ).distinct()

    context = {
        'categories' : categories,
        'bottom_categories' : categories[:7],
        'footer_categories' : footer_categories, 
        'business' : business,

    }
    return context
