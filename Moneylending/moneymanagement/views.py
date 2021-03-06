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
        countryname = Countries.objects.get(country_id=country).countryname
        if countryname == 'USA':
            addressline2= request.POST['addressline2']
        else:
            addressline2= request.POST.get('addressline2input', False);      
        city= request.POST['city']
        postalcode= request.POST['postalcode']
        email= request.POST['email']
        mobileno= int(request.POST['mobileno'])
        ssnno= request.POST['ssnno']
        phoneno= request.POST['phoneno']
        print(len(phoneno))
        if len(phoneno) < 1:
            phoneno = 0  
        password = 12345
        to_email = [email]
        #student = Student.objects.last()
        if User.objects.filter(username=email).exists():
            
            return render(request,'home.html',{'module':'register','messages' : 'User already exists'})
        else:
            
            User.objects.create_user(username=email,password=password,
                                    email=email,first_name=firstname,last_name=lastname)
            UserID= User.objects.last().id
            UserDetail = UserDetails(userID_id=UserID,dateofbirth=dateofbirth,mobilenumber=mobileno,
                                    phonenumber=phoneno)
           
            UserAddress  = Address(userID_id=UserID,addressLine1=addressline1,
                                    addressLine2=addressline2,city=city,postelCode=postalcode,
                                    ssnnNmber=ssnno,country=country)
            UserAddress.save()
            UserDetail.save()
            
            user = auth.authenticate(username=email,password=password)
            auth.login(request,user)
            request.session['userid'] = user.id
            request.session['useremail'] = user.email
            return render(request,'groups.html',{'module':'groups'})
    else:
         countries = Countries.objects.all()
         states = States.objects.all()
         return render(request,'home.html',{'module':'register','countries':countries,'states':states})
     
def login(request):
    if request.method == 'POST':
        email= request.POST['email']
        password= request.POST['password']
        user =auth.authenticate(username=email,password=password)        
        
        
        if user is not None:            
            auth.login(request,user)
            request.session['userid'] = user.id
            request.session['useremail'] = user.email
            return render(request,'groups.html',{'module':'groups'})
        else:            
            return render(request,'home.html',{'module':'login','messages':'Invalid Username or Password'})
            
        
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
            groups = GroupDescription.objects.filter(createBy=userid,isActive=1)
            return render(request,'useractivity.html',{'module':'invitegroup','groups':groups,'message':'You  have already active group'})
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
            userid = request.session['userid']
            groups = GroupDescription.objects.filter(createBy=userid,isActive=1)
            return render(request,'useractivity.html',{'module':'invitegroup','groups':groups})
        
    else:
        periodtypes = Periodtype.objects.all()
        return render(request,'useractivity.html',{'module':'creategroup','periodtypes':periodtypes})

def editprofile(request):
    userid = request.session['userid']
    if request.method == 'POST':
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        addressline1= request.POST['addressline1']
        addressline2= request.POST['addressline2']
        city= request.POST['city']
        postalcode= request.POST['postalcode']
       
        mobileno= int(request.POST['mobileno'])
        message =''
        phoneno= request.POST['phoneno']
        print(len(phoneno))
        if len(phoneno) < 1:
            phoneno = 0      
        
        User.objects.filter(id=userid).update(first_name=firstname,last_name=lastname)
        UserDetails.objects.filter(userID__pk=userid).update(mobilenumber=mobileno,
                                                             phonenumber=phoneno) 
        Address.objects.filter(userID__pk=userid).update(addressLine1=addressline1,addressLine2=addressline2
                                                         ,city=city,postelCode=postalcode)   
        message='Profile Updated successfully'
    
    UserDetail = UserDetails.objects.get(userID__pk=userid)
    UserAddress = Address.objects.get(userID__pk=userid)
    countryname = Countries.objects.get(country_id=UserAddress.country).countryname
    if request.method == 'POST':
        return render(request,'useractivity.html',{'message':message,'module':'editprofile','UserDetail':UserDetail,'Address':UserAddress})
    else:
        return render(request,'useractivity.html',{'module':'editprofile','UserDetail':UserDetail,'Address':UserAddress,'countryname':countryname})
        
def payoutorder(request):    
    userid = request.session['userid']
        
    if request.method == 'POST':
         count=0
         payoutlists = GroupDetails.objects.filter(isActive =1 )
         for payoutlist in payoutlists:            
             payoutorder = request.POST[payoutlist.Username]
             GroupDetails.objects.filter(isActive =1,Username=payoutlist.Username).update(payoutOrder=payoutorder)
             count +=1  
        
         return render(request,'groups.html',{'module':'groups'})       
    else:
        payoutlists = GroupDetails.objects.filter(isActive =1 )    
        return render(request,'useractivity.html',{'module':'payoutorder','payoutlists':payoutlists})

def myinvitation(request,invitestatus=0,groupID=0):
    email = request.session['useremail']
    userid = request.session['userid'] 
    if request.method == 'GET' and invitestatus != 0 and groupID != 0:
        if Settings.objects.filter(id =1).exists():            
            maxgroupcount = Settings.objects.get(id=1).maximumgroup
        else:
            maxgroupcount =10         
        
        groupcount =GroupDetails.objects.filter(id=groupID).count()        
        if invitestatus == 1 and maxgroupcount <= groupcount :
            groupdetails = GroupDescription.objects.filter(id=groupID).get()
            GroupDetail = GroupDetails(userID =userid,payStatus=0,payoutOrder=0,
                                       Username= email,Createby=groupdetails.createBy,isActive=groupdetails.isActive,groupdescpID=groupID)
            GroupDetail.save()
            InvitationDetails.objects.filter(emailID=email,isInvite=1,groupID=groupID).update(isInvite=0)
        else:
            InvitationDetails.objects.filter(emailID=email,isInvite=1,groupID=groupID).update(isInvite=0)
            invitations=InvitationDetails.objects.filter(emailID=email,isInvite=1)
            return render(request,'useractivity.html',{'module':'myinvitation','invitations':invitations,'message':'You are late to accept this inviation'})
            
    invitations=InvitationDetails.objects.filter(emailID=email,isInvite=1)
    return render(request,'useractivity.html',{'module':'myinvitation','invitations':invitations,'message':'hi'})

def invitegroup(request):  
    userid = request.session['userid']
    groups=GroupDescription.objects.filter(createBy=userid,isActive=1)
    if GroupDescription.objects.filter(createBy=userid,isActive=1).exists():       
        if request.method == 'POST':  
            groupdesc= GroupDescription.objects.get(createBy=userid,isActive=1)    
            email = request.POST['invitemail']
            groupID = groupdesc.pk            
            if InvitationDetails.objects.filter(groupID=groupID,emailID=email,isInvite=1).exists():
                return render(request,'useractivity.html',{'module':'invitegroup','groups':groups,'message':'Invitation already send'})
            else: 
                invitation =InvitationDetails(groupID=groupID,emailID=email,isInvite=1)
                invitation.save()
                return render(request,'useractivity.html',{'module':'invitegroup','groups':groups,'message':'Invitaion send Successfully'})
        else:
            return render(request,'useractivity.html',{'module':'invitegroup','groups':groups})
    else:
        return render(request,'useractivity.html',{'module':'invitegroup','groups':groups,'message':'You have not active group'})
            
        
def following(request):
    userid = request.session['userid']
    usergroups = GroupDescription.objects.filter(createBy=userid,isActive=1)
    return render(request,'useractivity.html',{'module':'following','groups':usergroups})


def follower(request):
    return render(request,'useractivity.html',{'module':'follower'})

def newcardregistor(request):
    return render(request,'usercard.html',{'module':'newcardregistor'})

def activegroups(request):
    groupdetails = GroupDescription.objects.filter(isActive=1)
    return render(request,'admin.html',{'module':'activegroup','groupdetails':groupdetails})

def setting(request):
    if request.method == 'POST':
        mingroup= request.POST['mingroup']
        maxgroup= request.POST['maxgroup']
        periodtype= request.POST['periodtype']
        if Settings.objects.filter(id =1).exists():
            Settings.objects.filter(id =1).update(minimumgroup=mingroup,maximumgroup=maxgroup)
            periodtype =Periodtype(periodtypename=periodtype)
            periodtype.save()
        else:
            groupsetting =Settings(minimumgroup=mingroup,maximumgroup=maxgroup)
            periodtype =Periodtype(periodtypename=periodtype)
            periodtype.save()
            groupsetting.save()        
        return render(request,'admin.html',{'module':'setting','message':'setting insert successfully'})
        
    else:
        return render(request,'admin.html',{'module':'setting'})

def userlist(request):
    users = User.objects.all()
    return render(request,'admin.html',{'module':'userlist','Users':users})