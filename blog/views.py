from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from blog.models import BlogComment, BlogPost
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.
def index(request):
    myblogs=BlogPost.objects.all()
    params={"myblogs":myblogs}
    return render(request,"blog/index.html",params)

def createblog(request):
    return render(request,"blog/editor.html")

def BlogPostLike(request, pk):
    post = get_object_or_404(BlogPost, blog_id=request.POST.get("blogpost_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blogpost', args=[str(pk)]))

def blogpost(request,blogid):
    post=BlogPost.objects.get(blog_id=blogid)
    comments=BlogComment.objects.filter(post=post)
    query_set=BlogPost.objects.all()
    total_likes=post.number_of_likes()
    params={"post":post,"range":len(query_set),"comments":comments,"total_likes":total_likes}
    return render(request,"blog/blogpost.html",params)

def search(request):
    messages.success(request, "Search results: ")
    query=request.POST.get("query")
    if len(query)>60:
        searchpost=BlogPost.objects.none()
    else:
        q_author=BlogPost.objects.filter(author__icontains=query)
        q_title=BlogPost.objects.filter(title__icontains=query)
        q_category=BlogPost.objects.filter(category__icontains=query)
        q_heading1=BlogPost.objects.filter(heading1__icontains=query)
        q_content1=BlogPost.objects.filter(content1__icontains=query)
        q_heading2=BlogPost.objects.filter(heading2__icontains=query)
        q_content2=BlogPost.objects.filter(content2__icontains=query)
        q_about=BlogPost.objects.filter(about__icontains=query)
        searchpost=q_author.union(q_title,q_category,q_heading1,q_content1,q_heading2,q_content2,q_about)
    if searchpost.count()==0:
        messages.warning(request, "No search results found.")
    params={"searchposts":searchpost,"query":query}
    return render(request, "blog/search.html",params)

def blog_ideas(request):
    return render(request,"blog/Blog_Ideas.html")

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

def postcomment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postId=request.POST.get("postId")
        post=BlogPost.objects.get(blog_id=postId)
        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,"Your comment is posted successfully.")
    return redirect(f"/blogs/blogpost/{postId}")