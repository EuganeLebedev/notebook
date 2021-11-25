from django import forms
from articles.models import Post, Category
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_content', 'categoryes']

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Заголовок'
            }),
            'post_content': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Пост'
            }),
            'categoryes': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'title': _('Заголовок'),
            'post_content': _('Текст поста'),
            'categoryes': _('Категория'),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Категория'
            }),
        }
