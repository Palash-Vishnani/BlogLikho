from django.db import models
from django.utils.timezone import now

# Create your models here.
class BlogPost(models.Model):
    blog_id=models.AutoField(primary_key=True)
    author=models.CharField(max_length=200)
    title=models.CharField(max_length=300)
    pub_date=models.DateField()
    heading1=models.CharField(max_length=300)
    content1=models.TextField()
    heading2=models.CharField(max_length=300)
    content2=models.TextField()
    about=models.TextField()
    image=models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.title + " by " + self.author
