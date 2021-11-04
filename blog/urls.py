from django.urls.resolvers import URLPattern
from . import views
from django.urls import path


urlpatterns=[
    path('',views.index,name='bloghome'),
    path("blogs/createblog",views.createblog,name="createblog"),
    path('blogpost/<int:blogid>',views.blogpost,name="blogpost"),
    path("search",views.search,name="search"),
    path("blog_ideas",views.blog_ideas,name="blog_ideas"),
    path("signup",views.handleSignup,name="signup"),
    path("login",views.handleLogin,name="login"),
    path("logout",views.handleLogout,name="logout"),
    path("blogpost-like/<int:pk>",views.BlogPostLike,name="blogpost_like"),
    # API to post a comment
    path("postcomment",views.postcomment,name="postcomment")
]