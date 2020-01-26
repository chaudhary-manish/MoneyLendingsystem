from django.urls import path

from . import views

urlpatterns = [
      path('',views.home,name="home"),
      path('home',views.home,name="home"),
      path('login',views.login,name="login"),
      path('logout',views.logout,name="logout"),
      path('following',views.following,name="following"),
      path('follower',views.follower,name="follower"),
      path('groups',views.groups,name="groups"),
      path('creategroup',views.creategroup,name="creategroup"),
      path('editprofile',views.editprofile,name="editprofile"),
      path('invitegroup',views.invitegroup,name="invitegroup"),
      path('contact',views.contact,name="contact"),
      path('register',views.register,name="register"),
      path('myinvitation',views.myinvitation,name="myinvitation"),
      path('myinvitation/<int:invitestatus>/<int:groupID>/',views.myinvitation,name="myinvitation"),
      path('payoutorder',views.payoutorder,name="payoutorder"),
      path('newcardregistor',views.newcardregistor,name="newcardregistor"),
      path('activegroups',views.activegroups,name="activegroups"),
      path('setting',views.setting,name="setting"),
      path('userlist',views.userlist,name="userlist")
    
]