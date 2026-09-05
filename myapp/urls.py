from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
     path('',views.home),
     path('about', views.about, name='about'),
     path('register',views.register, name='register'),
     path('formsave',views.formsave),
     path('viewdata',views.viewdata),
     path('deletestudent/int:id',views.deletestudent),
     path('updatestudent', views.updatestudent, name='updatestudent'),
     path('profileupdate',views.profileupdate,name='profileupdate'),
     path('login',views.login,name='login'),
     path('dashboard',views.dashboard,name='dashboard'),
]
