from django.forms import ModelForm
from .models import Article, Category, ArticleImage

class ImageCreateForm(ModelForm):
    class Meta:
        model = ArticleImage
        fields = '__all__'


class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
