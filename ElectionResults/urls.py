from django.urls import path

from . import views

urlpatterns = [
    path('', views.PollingUnitResultList.as_view(), name='polling_unit_results'),
]