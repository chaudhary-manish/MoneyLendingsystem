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
    addressLine1 = models.CharField(max_length=30)
    addressLine2= models.CharField(max_length=30)    
    city = models.CharField(max_length=20)
    postelCode=models.BigIntegerField()   
    ssnnNmber=models.BigIntegerField()
    country = models.CharField(max_length=30)

class GroupDescription(models.Model):
    id = models.AutoField(primary_key=True)
    groupName = models.CharField(max_length=30)
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

class MonthlyPaymentDetails(models.Model):
    id = models.AutoField(primary_key=True) 
    groupID = models.IntegerField()  
    userID = models.IntegerField()
    paidFrequency = models.IntegerField()
    paidDate = models.DateField()

class InvitationDetails(models.Model):
    id = models.AutoField(primary_key=True) 
    groupID = models.IntegerField()  
    emailID = models.CharField(max_length=30)
    isInvite=models.IntegerField() 

class UserRating(models.Model):
    userID = models.IntegerField()
    userPoint = models.IntegerField()   
    
class UserbankDetails(models.Model):
    id = models.AutoField(primary_key=True) 
    userID = models.IntegerField()
    bankaddress = models.IntegerField() 
    bankname =models.CharField(max_length=30)
    accountnumer=models.IntegerField()
    ifscCode=  models.CharField(max_length=30) 
   
   
   
