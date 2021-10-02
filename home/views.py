from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from home.models import Contact

# Create your views here.
def index(request):
    return render(request,"home/index.html")

def about(request):
    return render(request,"home/About.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        check1=request.POST.get("check1",default="off")
        check2=request.POST.get("check2",default="off")
        check3=request.POST.get("check3",default="off")
        check4=request.POST.get("check4",default="off")
        feedback=request.POST.get("feedback")
        if len(name)<2 or len(email)<4 or len(feedback)<2:
            messages.warning(request,"Please fill out all the fields correctly.")
        else:
            contact_message=Contact(name=name,email=email,number=phone,check1=check1,check2=check2,check3=check3,check4=check4,feedback=feedback)
            contact_message.save()
            messages.success(request,"Thanks for your query or feedback.")
    return render(request,"home/ContactUs.html")