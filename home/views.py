from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import BlogPost

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

def search(request):
    messages.success(request, "Search results: ")
    query=request.POST.get("query")
    if len(query)>60:
        searchpost=BlogPost.objects.none()
    else:
        q_author=BlogPost.objects.filter(author__icontains=query)
        q_title=BlogPost.objects.filter(title__icontains=query)
        q_heading1=BlogPost.objects.filter(heading1__icontains=query)
        q_content1=BlogPost.objects.filter(content1__icontains=query)
        q_heading2=BlogPost.objects.filter(heading2__icontains=query)
        q_content2=BlogPost.objects.filter(content2__icontains=query)
        q_about=BlogPost.objects.filter(about__icontains=query)
        searchpost=q_author.union(q_title,q_heading1,q_content1,q_heading2,q_content2,q_about)
    if searchpost.count()==0:
        messages.warning(request, "No search results found.")
    params={"searchposts":searchpost,"query":query}
    return render(request, "blog/search.html",params)

def blog_ideas(request):
    return render(request,"home/Blog_Ideas.html")

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


