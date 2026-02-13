from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.HealthRecordListView.as_view(),name = 'healthrecord_list'),
    path('<int:pk>/',views.HealthRecordDetailView.as_view(),name = 'healthrecord_detail'),
    path('new/',views.HealthRecordCreateView.as_view(),name='healthrecord_create'),
    path('<int:pk>/edit/',views.HealthRecordUpdateView.as_view(),name='healthrecord_update'),
    path('<int:pk>/delete/',views.HealthRecordDeleteView.as_view(),name='healthrecord_delete'),
]
