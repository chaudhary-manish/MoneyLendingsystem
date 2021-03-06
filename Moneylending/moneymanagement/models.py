from django.db import models
from  django.contrib.auth.models import User,Group

# Create your models here.

class UserDetails(models.Model):   
    userID = models.OneToOneField(User,on_delete=models.CASCADE)
    dateofbirth=models.DateField(max_length=8 , null=True, blank=True)    
    mobilenumber=models.BigIntegerField()    
    phonenumber=models.BigIntegerField()
    profilepic=models.ImageField(null=True, blank=True)

class Address(models.Model):
    userID = models.OneToOneField(User,on_delete=models.CASCADE)  
    addressLine1 = models.TextField(max_length=30)
    addressLine2= models.TextField(max_length=30)    
    city = models.TextField(max_length=20)
    postelCode=models.BigIntegerField()   
    ssnnNmber=models.TextField(null=True)
    country = models.TextField(max_length=30)

class GroupDescription(models.Model):
    id = models.AutoField(primary_key=True)
    groupName = models.TextField(max_length=30)
    payments= models.CharField(max_length=30)    
    paymentsFrequency = models.CharField(max_length=10) 
    startDate=models.DateField(max_length=12)   
    noofperiod=models.IntegerField(null=True)
    createBy = models.IntegerField()
    isActive = models.IntegerField()

class GroupDetails(models.Model):
    id = models.AutoField(primary_key=True)      
    userID = models.IntegerField()
    payStatus = models.IntegerField()   
    payoutOrder = models.IntegerField()
    groupdescpID = models.IntegerField()
    Username = models.TextField()
    Createby = models.IntegerField()
    isActive = models.IntegerField()
    
class MonthlyPaymentDetails(models.Model):
    id = models.AutoField(primary_key=True) 
    groupID = models.IntegerField()  
    userID = models.IntegerField()
    paidFrequency = models.IntegerField()
    paidDate = models.DateField()

class InvitationDetails(models.Model):
    id = models.AutoField(primary_key=True) 
    groupID = models.IntegerField()  
    emailID = models.TextField(max_length=30)
    isInvite=models.IntegerField() 

class UserRating(models.Model):
    userID = models.IntegerField()
    userPoint = models.IntegerField()   
    
class UserbankDetails(models.Model):
    id = models.AutoField(primary_key=True) 
    userID = models.IntegerField()
    bankaddress = models.TextField() 
    bankname =models.TextField(max_length=30)
    accountnumer=models.IntegerField()
    ifscCode=  models.TextField(max_length=30) 
    
class Countries(models.Model):
    id = models.AutoField(primary_key=True) 
    countryID=models.TextField(max_length=30)
    countryname=models.TextField(max_length=30)
    
    
class Settings(models.Model):
    id = models.AutoField(primary_key=True) 
    minimumgroup=models.IntegerField(default=3)
    maximumgroup=models.IntegerField(default=3)
    
class Periodtype(models.Model):
    id = models.AutoField(primary_key=True) 
    periodtypename=models.TextField(max_length=30)

class States(models.Model):
    states_id = models.AutoField(primary_key=True) 
    states_code=models.TextField(max_length=30)
    states_name=models.TextField(max_length=30)
   
    
    
   
   
   
