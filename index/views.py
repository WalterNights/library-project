from library_app.models import User, Book
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView

# Create your views here.
class IndexView(TemplateView):
    model = User
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context