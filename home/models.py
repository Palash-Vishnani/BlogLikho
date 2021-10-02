from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    number=models.IntegerField()
    check1=models.CharField(max_length=50)
    check2=models.CharField(max_length=50)
    check3=models.CharField(max_length=50)
    check4=models.CharField(max_length=50)
    feedback=models.TextField()

    def __str__(self):
        return "message by " + self.name
