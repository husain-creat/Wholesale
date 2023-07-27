from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.log, name='loginPage'),
    path('login', views.login, name='logged'),
    path('home',views.home , name='mainPage'),
    path('reg', views.reg, name = 'reg'),
    path('logout', views.logout, name='logout'),
    path('signup', views.companyform), # this link for company form page
    path('salesrep', views.salesrepform),# this link is for sales representative form page

]