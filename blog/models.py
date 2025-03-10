from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.forms import IntegerField
from django.template.defaulttags import now


# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    bio = models.TextField()
    text = models.TextField()
    subjects = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    student = models.CharField(max_length=100)

    def str(self):
         return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def str(self):
        return self.name

class Lenov(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    chegirma = models.CharField(max_length=200)

    def str(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = IntegerField()
    messege = models.TextField()

    def str(self):
        return self.name

class Your_email(models.Model):
    email = models.EmailField()

    def str(self):
        return self.email

class Shadow(models.Model):
    bio = models.TextField()
    img = models.ImageField(upload_to='index/img')
    price = models.CharField(max_length=200)

    def str(self):
        return self.bio

class Comment(models.Model):
    clas = models.ForeignKey(Shadow, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    created_et = models.DateTimeField(default=now, null=True, blank=True )

    def str(self):
        return f"{self.user.username} - {self.clas.name}"





class Forma(models.Model):
    DESTINATION_CHOISE={
        'usa':'Usa',
        'mexico':'Mexico',
        'china':'China',
        'japan':'Japan',
        'italiy':'Italiy'

    }
    name = models.CharField(max_length=200)
    email = models.EmailField()
    destination = models.CharField(max_length=100,choices=DESTINATION_CHOISE,default='usa')
    request = models.TextField(blank=True,null=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.name























