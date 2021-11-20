from django.urls import path
from articles import views


urlpatterns = [
    path('create', views.PostCreate.as_view(), name='post_create'),
    path('category_create', views.CategoryCreate.as_view(), name='category_create')
]
