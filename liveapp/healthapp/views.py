from django.shortcuts import render
from. import models
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import HealthRecordForm


# Create your views here.
class HealthRecordListView(ListView):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_list.html'
    context_object_name = 'healthrecords'

class HealthRecordDetailView(DetailView):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_detail.html'
    context_object_name = 'healthrecord'

class HealthRecordCreateView(CreateView):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_create.html'
    form_class = HealthRecordForm
    success_url = reverse_lazy('healthrecord_list')

class HealthRecordUpdateView(UpdateView):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_update.html'
    form_class = HealthRecordForm
    success_url = reverse_lazy('healthrecord_list')

class HealthRecordDeleteView(DeleteView):
    model = models.HealthRecord
    template_name = 'healthapp/healthrecord_delete.html'
    success_url = reverse_lazy('healthrecord_list')
