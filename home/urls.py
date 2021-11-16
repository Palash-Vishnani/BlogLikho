from django.urls import path
from django.contrib import admin
from django.urls.resolvers import URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.index,name="homepage"),
    path("About",views.about,name="about"),
    path("blogs/createblog",views.createblog,name="createblog"),
    path("ContactUs",views.contact,name="contact"),
    path("blogs/search",views.search,name="search"),
    path("blogs/blog_ideas",views.blog_ideas,name="blog_ideas"),
    path("signup",views.handleSignup,name="signup"),
    path("login",views.handleLogin,name="login"),
    path("logout",views.handleLogout,name="logout")
]