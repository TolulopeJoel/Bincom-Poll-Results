from django.urls import path

from . import views

urlpatterns = [
    path('', views.PollingUnitResultList.as_view(), name='polling_unit_results'),
    path('lga/', views.lga_total_results_view, name='lga_total_results'),
]