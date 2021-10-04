from django.urls.resolvers import URLPattern
from . import views
from django.urls import path


urlpatterns=[
    path('',views.index,name='bloghome'),
    path('blogpost/<int:blogid>',views.blogpost,name="blogpost"),
]