from django.urls import path

from . import views

app_name = "mainsite"

urlpatterns = [
    #path("", views.welcome, name="home"), #go to views.index
    path("login", views.login, name="login"),
    path("", views.home, name="home"),
    path("search/<str:pk>", views.searchpage, name="search"),
    path("about", views.about_us, name="aboutus"),
    path("contact", views.contact, name="contact"),

    path("create", views.createlab, name='newlab'),
]