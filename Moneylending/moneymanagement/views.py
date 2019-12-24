from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth,Group
from django.conf import settings
from moneymanagement.models import *

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
        city= request.POST['city']
        postalcode= request.POST['postalcode']
        email= request.POST['email']
        mobileno= request.POST['mobileno']
        ssnno= request.POST['ssnno']
        phoneno= request.POST['phoneno']
        password = 12345
        to_email = [email]
        #student = Student.objects.last()
        if User.objects.filter(username=email).exists():
            print('user exist')
            return render(request,'home.html',{'module':'register'})
        else:
            User.objects.create_user(username=email,password=password,
                                    email=email,first_name=firstname,last_name=lastname)
            UserID= User.objects.last().id
            UserDetail = UserDetails(userID_id=UserID,dateofbirth=dateofbirth,mobilenumber=mobileno,
                                    phonenumber=phoneno)
            UserDetail.save()
            UserAddress  = Address(userID_id=UserID,addressLine1=addressline1,
                                    addressLine2=addressline2,city=city,postelCode=postalcode,
                                    ssnnNmber=ssnno,country=country)
            UserAddress.save()
            send_mail('Your auto generated password', '12345', 'sd2009002@rediffmail.com', to_email, fail_silently=False)
            user = auth.authenticate(username=email,password=password)
            auth.login(request,user)
            return render(request,'groups.html',{'module':'groups'})
    else:
         return render(request,'home.html',{'module':'register'})
     
def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        user =auth.authenticate(username=email,password=password)        
        
        if User is not None:            
            auth.login(request,user)
            request.session['userid'] = user.id
            request.session['useremail'] = user.email
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
    if request.method == 'POST':
        userid = request.session['userid']
        if GroupDescription.objects.filter(createBy=userid,isActive=1).exists():
            return render(request,'useractivity.html',{'module':'invitegroup','message':'You  have already active group'})
        else:    
            GroupName = request.POST['GroupName']
            payments = request.POST['payments']
            payfrequency = request.POST['payfrequency']
            startdate = request.POST['startdate']
            noofperiod = request.POST['noofperiod']            
            GroupDesc = GroupDescription(groupName=GroupName,payments=payments,
                                        paymentsFrequency=payfrequency,startDate=startdate
                                        ,noofperiod=noofperiod,createBy=userid,isActive=1)
            GroupDesc.save()
            return render(request,'useractivity.html',{'module':'invitegroup'})
        
    else:
        return render(request,'useractivity.html',{'module':'creategroup'})

def editprofile(request):
    return render(request,'useractivity.html',{'module':'editprofile'})

def invitegroup(request):
    # userid = updetails={}
    # grrequest.session['userid']
    # usergroups = GroupDescription.objects.filter(createBy=userid,isActive=1).only('groupName')
    # grooupdetails['module'] = 'invitegroup'
    # groupdetails['usergroups'] = usergroups
    userid = request.session['userid']
    groups = GroupDescription.objects.filter(createBy=userid,isActive=1)
    return render(request,'useractivity.html',{'module':'invitegroup','groups':groups})

def following(request):
    userid = request.session['userid']
    usergroups = GroupDescription.objects.filter(createBy=userid,isActive=1)
    return render(request,'useractivity.html',{'module':'following','groups':usergroups})


def follower(request):
    return render(request,'useractivity.html',{'module':'follower'})
