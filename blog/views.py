from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render,redirect
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    myblogs=BlogPost.objects.all()
    params={"myblogs":myblogs}
    return render(request,"blog/index.html",params)

def blogpost(request,blogid):
    post=BlogPost.objects.get(blog_id=blogid)
    query_set=BlogPost.objects.all()
    params={"post":post,"range":len(query_set)}
    return render(request,"blog/blogpost.html",params)

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
            return redirect("/blogs")
        elif len(username) > 20:
            messages.warning(request, "Signup failed..Enter a short and precise username.")
            return redirect("/blogs")
        elif not username.isalnum():
            messages.warning(request, "Ooops..Username should contain letters and numbers. Please try again.")
            return redirect("/blogs")
        elif not fname.isalpha() or not lname.isalpha():
            messages.warning(request, "Signup failed..First name and last name should only contain letters. Try again.")
            return redirect("/blogs")
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
            return redirect("/blogs")
    else:
        return HttpResponse("Error 404 - Page not found.")

def handleLogout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("/blogs")
