from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        country= request.POST['country']
        dateofbirth= request.POST['dateofbirth']
        addressline1= request.POST['addressline1']
        addressline2= request.POST['addressline2']
        company= request.POST['company']
        city= request.POST['city']
        postalcode= request.POST['postalcode']
        email= request.POST['email']
        mobileno= request.POST['mobileno']
        ssnno= request.POST['ssnno']
        phoneno= request.POST['phoneno']
        password = 12345
        
        if User.objects.filter(username=email).exists():
            print('user exist')
        else:
           User.objects.create_user(username=email,password=password,
                                    email=email,first_name=firstname,last_name=lastname)
           return render(request,'home.html',{'module':'register'})
    else:
         return render(request,'home.html',{'module':'register'})
     
def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        user =auth.authenticate(username=email,password=password)
        if User is not None:
            auth.login(request,user)
            return render(request,'groups.html',{'module':'groups'})
        else:
            print('bad credintual')
            return render(request,'home.html',{'module':'login'})
            
        
        # send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
        #  ['to@example.com'], fail_silently=False)
    return render(request,'home.html',{'module':'login'})

def logout(request):
    auth.logout(request)
    return render(request,'home.html',{'module':'login'})
                  
def contact(request):
    return render(request,'home.html',{'module':'contact'})

def groups(request):
    return render(request,'groups.html',{'module':'groups'})

def creategroup(request):
    return render(request,'useractivity.html',{'module':'creategroup'})

def editprofile(request):
    return render(request,'useractivity.html',{'module':'editprofile'})

def invitegroup(request):
    return render(request,'useractivity.html',{'module':'invitegroup'})
