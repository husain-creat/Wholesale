from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('signup', views.companyform), # this link for company form page
    path('salesrep', views.salesrepform),# this link is for sales representative form page
    

  ]