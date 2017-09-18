from django.contrib import messages
from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'base.html'
