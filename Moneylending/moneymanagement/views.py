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
        
        if User.objects.filter(username=email).exists():
            print('email exits')
            send_mail(
            'Subject here',
            'Here is the message.',
            'chaudhary94rc@gmail.com',
            'chaudhary94rc@gmail.com',
            fail_silently=False,)
        else:
            print(firstname)
            return render(request,'home.html',{'module':'register'})
    else:
         return render(request,'home.html',{'module':'register'})
     
def login(request):
    if request.method == 'POST':
        send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
         ['to@example.com'], fail_silently=False)
    return render(request,'home.html',{'module':'login'})

def contact(request):
    return render(request,'home.html',{'module':'contact'})
