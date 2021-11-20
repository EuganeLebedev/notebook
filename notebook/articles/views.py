from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from articles.models import Post
# Create your views here.


class PostCreate(CreateView):
    model = Post
    template_name = 'articles/post_create.html'
    fields = ['title', 'post_content', 'categoryes']


class PostShow(DetailView):
    pass


class PostDelete(DeleteView):
    pass


class PostList(ListView):
    pass
