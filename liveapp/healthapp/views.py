from django.shortcuts import render
from. import models
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import HealthRecordForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HealthRecordListView(LoginRequiredMixin,ListView):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_list.html'
    context_object_name = 'healthrecords'
    def get_queryset(self):
        return models.HealthRecord.objects.filter(user=self.request.user)

class HealthRecordDetailView(LoginRequiredMixin,DetailView):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_detail.html'
    context_object_name = 'healthrecord'
    def get_queryset(self):
        return models.HealthRecord.objects.filter(user=self.request.user)

class HealthRecordCreateView(LoginRequiredMixin,CreateView):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_create.html'
    form_class = HealthRecordForm
    success_url = reverse_lazy('healthrecord_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HealthRecordUpdateView(UpdateView,LoginRequiredMixin):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_update.html'
    form_class = HealthRecordForm
    success_url = reverse_lazy('healthrecord_list')
    def get_queryset(self):
        return models.HealthRecord.objects.filter(user=self.request.user)
class HealthRecordDeleteView(DeleteView,LoginRequiredMixin):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_delete.html'
    success_url = reverse_lazy('healthrecord_list')
    def get_queryset(self):
        return models.HealthRecord.objects.filter(user=self.request.user)
