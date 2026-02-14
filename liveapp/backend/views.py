from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'home.html'

class DashboardPageView(TemplateView,LoginRequiredMixin):
    template_name='dashboard.html'