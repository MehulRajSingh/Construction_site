# services/urls.py
from django.urls import path
from . import views

app_name = 'services'  # This is important for namespace

urlpatterns = [
    path('', views.services_view, name='services'),  # Make sure this name is 'services'
]