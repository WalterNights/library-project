from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Create your views here.

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
class DashboardView(ListView):
    template_name = "dashboard.html"
    model = User
    context_object_name = None
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        context['user_list'] = users
        return context