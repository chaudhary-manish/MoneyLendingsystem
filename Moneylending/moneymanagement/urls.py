from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
     path('home',views.home,name="home"),
     path('login',views.login,name="login"),
      path('contact',views.contact,name="contact"),
    path('register',views.register,name="register")
    
]