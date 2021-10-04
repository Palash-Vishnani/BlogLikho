from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

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

def handleSignup(request):
    if request.method=="POST":
        username=request.POST.get("username")
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")
        if pass1!=pass2:
            messages.warning(request, "Ooops..Passwords do not match. Please try again.")
            return redirect("/")
        elif len(username) > 20:
            messages.warning(request, "Signup failed..Enter a short and precise username.")
            return redirect("/")
        elif not username.isalnum():
            messages.warning(request, "Ooops..Username should contain letters and numbers. Please try again.")
            return redirect("/")
        elif not fname.isalpha() or not lname.isalpha():
            messages.warning(request, "Signup failed..First name and last name should only contain letters. Try again.")
            return redirect("/")
        else:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your Account is Created Successfully.")
            return redirect("/blogs")
    else:
        return HttpResponse("Error 404 - Page Not Found.")

def handleLogin(request):
    if request.method=="POST":
        username2=request.POST.get("name")
        password=request.POST.get("password")
        user = authenticate(username=username2, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hello {user} you are successfully logged in.")
            return redirect("/blogs")
        else:
            messages.warning(request, "Please enter valid username, email address and password.")
            return redirect("/")
    else:
        return HttpResponse("Error 404 - Page not found.")

def handleLogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("/")


