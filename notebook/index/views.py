from django.shortcuts import render
from django.views.generic import TemplateView
from index.models import Regards

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["regards_images"] = Regards.objects.all()
        return context
