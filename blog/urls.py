from django.urls.resolvers import URLPattern
from . import views
from django.urls import path


urlpatterns=[
    path('',views.index,name='bloghome'),
    path('blogpost/<int:blogid>',views.blogpost,name="blogpost"),
    path("search",views.search,name="search"),
    path("signup",views.handleSignup,name="signup"),
    path("login",views.handleLogin,name="login"),
    path("logout",views.handleLogout,name="logout"),
    path("blogpost-like/<int:pk>",views.BlogPostLike,name="blogpost_like"),
    # API to post a comment
    path("postcomment",views.postcomment,name="postcomment")
]