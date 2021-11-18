import PIL
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    blog_id=models.AutoField(primary_key=True)
    author=models.CharField(max_length=200)
    title=models.CharField(max_length=300)
    pub_date=models.DateField()
    category=models.CharField(max_length=200,default="Promotional Blogs")
    heading1=models.CharField(max_length=300,blank=True)
    content1=models.TextField(blank=True)
    heading2=models.CharField(max_length=300)
    # content2=models.TextField()
    content2=RichTextField(blank=True,null=True)
    about=models.TextField()
    likes=models.ManyToManyField(User, related_name="blogpost_like")
    image=models.ImageField(upload_to="blog/images")
    linkedin_link=models.CharField(max_length=500,blank=True)
    other_link=models.CharField(max_length=500,blank=True)
  
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " by " + self.author

    def get_absolute_url(self):
        return reverse('createblog',args=(str(self.blog_id)))

class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:10] + "..." + "by " + self.user.username
