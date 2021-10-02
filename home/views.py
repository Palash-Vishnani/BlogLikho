from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home/index.html")

def about(request):
    return render(request,"home/About.html")

def contact(request):
    return render(request,"home/ContactUs.html")