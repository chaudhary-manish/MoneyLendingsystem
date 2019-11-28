from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name="home"),
     path('home',views.home,name="home"),
     path('login',views.login,name="login"),
     path('logout',views.logout,name="logout"),
     path('groups',views.groups,name="groups"),
     path('creategroup',views.creategroup,name="creategroup"),
      path('editprofile',views.editprofile,name="editprofile"),
      path('invitegroup',views.invitegroup,name="invitegroup"),
      path('contact',views.contact,name="contact"),
    path('register',views.register,name="register")
    
]