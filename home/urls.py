from django.urls import path
from django.contrib import admin
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path("About",views.about,name="about"),
    path("ContactUs",views.contact,name="contact"),
]