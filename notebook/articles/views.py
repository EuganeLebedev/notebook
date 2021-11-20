from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from articles.forms import PostForm, CategoryForm
# Create your views here.


class PostCreate(CreateView):
    # model = Post
    form_class = PostForm
    template_name = 'articles/post_create.html'


class PostShow(DetailView):
    pass


class PostDelete(DeleteView):
    pass


class PostList(ListView):
    pass


class CategoryCreate(CreateView):
    # model = Post
    form_class = CategoryForm
    template_name = 'articles/post_create.html'
