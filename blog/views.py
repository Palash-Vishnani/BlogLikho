from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.
def index(request):
    myblogs=BlogPost.objects.all()
    params={"myblogs":myblogs}
    return render(request,"blog/index.html",params)

