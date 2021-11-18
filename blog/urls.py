from django.urls.resolvers import URLPattern
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='bloghome'),
    path("createblog",views.createblog,name="createblog"),
    path("userprofile",views.userprofile,name="userprofile"),
    path("my_blogs",views.my_blogs,name="my_blogs"),
    path("popularblogs",views.popularblogs,name="popularblogs"),
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