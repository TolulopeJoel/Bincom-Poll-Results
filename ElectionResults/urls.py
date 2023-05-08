from django.urls import path

from . import views

urlpatterns = [
    path('', views.PollingUnitResultListView.as_view(), name='polling_unit_results'),
    path('lga/', views.lga_total_results_view, name='lga_total_results'),
    path('add-results/', views.AddPollingUnitResultView.as_view(), name='add_polling_unit_result'),
]