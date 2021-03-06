from django.shortcuts import render
from django.views.generic import TemplateView
from index.models import Regards, Category
from django.db.models import Count

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoryes"] = Category.objects.all()
        return context


class RegardsView(TemplateView):
    template_name = 'index/regards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoryes"] = Category.objects.all()
        return context
