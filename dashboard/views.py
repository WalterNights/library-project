from django.shortcuts import render
from library_app.models import User, Book
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView

# Create your views here.

def is_admin(user):
    return user.is_authenticated and user.is_staff

class DashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "dashboard/dashboard.html"
    model = User
    context_object_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        context['user_list'] = users
        return context
    
    def test_func(self):
        return self.request.user.is_staff