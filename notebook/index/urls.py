from django.urls import path
from index.views import IndexView, RegardsView

app_name = 'index'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('regards', RegardsView.as_view(), name='regards'),
]
