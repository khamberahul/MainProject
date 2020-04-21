from typing import Set, Any

from django.shortcuts import render


from .models import Post
from .models import data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages, auth
from django.template import loader
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'first post Content',
        'date_posted':'December 19,2019',
    },
    {
        'author': 'Rahul',
        'title': 'Blog Post 2',
        'content': 'Second post Content',
        'date_posted': 'December 20,2019',
    },
    {
        'author': 'Rahul1',
        'title': 'Blog Post 4',
        'content': ' post Content',
        'date_posted': 'march 20,2020',
    }
]
def hi(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request,'LoginApp/hi.html',context)

def about(request):
    return render(request,'LoginApp/about.html' ,{'title': 'About'})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "Logged out successfully!")
        return render(request,"LoginApp/login.html",{});
    return render(request, "LoginApp/hi.html", {});
def details(request):
    obj=data.objects.all()
    context={
        'objects':obj
    }
    return render(request,'LoginApp/details.html',context)

def booking(request,pk):
    obj = data.objects.get(pk=pk)
    object2 = data()
    object2.froms = obj.froms
    object2.tos = obj.tos
    object2.fare = obj.fare
    object2.classs = obj.classs

    return render(request,'LoginApp/Book.html',{'object2':object2})
def reservation(request):
    messages.success(request, "Your Ticket Booked Successfully !!!")
    return HttpResponseRedirect(reverse('home-page'))


