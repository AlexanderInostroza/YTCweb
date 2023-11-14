from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pets/", views.pets, name="pets"),
    path("donate/", views.donate, name="donate"),
    path("aboutUs/", views.aboutUs, name="aboutUs")
]