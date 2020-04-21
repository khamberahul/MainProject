from django.conf.urls import url
from django.contrib import admin

from django.urls import path
from .models import data
from.import views
urlpatterns = [
    path('', views.hi , name='home-page'),
    path('contact_us/', views.about , name='home-about'),
    path('reservation/',views.details,name='details'),
    url(r'(?P<pk>\d+)/$',views.booking,name= 'booking'),
    path('booked/',views.reservation,name='home')
];