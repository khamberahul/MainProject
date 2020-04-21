from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class data(models.Model):
    froms = models.CharField(max_length=100)
    tos = models.CharField(max_length=100)
    fare = models.IntegerField()
    classs = models.CharField(max_length=100)

    def __str__(self):
        return self.froms

class book(models.Model):
    user = models.CharField(max_length=100)
    froms = models.CharField(max_length=100)
    tos = models.CharField(max_length=100)
    fare = models.IntegerField()
    classs = models.CharField(max_length=100)