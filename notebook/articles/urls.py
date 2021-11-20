from django.urls import path
from articles import views


urlpatterns = [
    path('', views.PostCreate.as_view(), name='post_create')
]
