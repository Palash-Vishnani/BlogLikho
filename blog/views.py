from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"blog/index.html")

