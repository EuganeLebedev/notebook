from django import forms
from articles.models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_content', 'categoryes']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
