# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),           # homepage
    path("about/", views.about, name="about"),   # about page
    path("contact/", views.contact, name="contact"),

    path("portfolio/", views.portfolio, name="portfolio"),
    
]

