from django.db import models
from  django.contrib.auth.models import User,Group

# Create your models here.

class UserDetails(models.Model):   
    userID = models.OneToOneField(User,on_delete=models.CASCADE)    
    company= models.CharField(max_length=30)    
    mobilenumber=models.IntegerField(max_length=10)    
    phoneenumber=models.IntegerField(max_length=10)
    profilepic=models.ImageField()

class Address(models.Model):
    userID = models.OneToOneField(User,on_delete=models.CASCADE)  
    addressLine1 = models.CharField(max_length=30)
    addressLine2= models.CharField(max_length=30)    
    city = models.CharField(max_length=20)
    postelCode=models.IntegerField(max_length=12)   
    ssnnNmber=models.IntegerField(max_length=9)
    country = models.CharField(max_length=30)

class GroupDescription(models.Model):
    groupID = models.OneToOneField(Group,on_delete=models.CASCADE)  
    groupName = models.CharField(max_length=30)
    payments= models.CharField(max_length=30)    
    paymentsFrequency = models.IntegerField(max_length=5)
    startDate=models.DateField(max_length=12)   
    endDate=models.DateField(max_length=9)
    createBy = models.IntegerField(max_length=30)
    isActive = models.IntegerField(max_length=1)

class GroupDetails(models.Model):
    groupdescID = models.ForeignKey(GroupDescription,on_delete=models.CASCADE)  
    userID = models.IntegerField(max_length=30)
    payStatus = models.IntegerField(max_length=1)   
    payoutOrder = models.IntegerField(max_length=30)

class MonthlyPaymentDetails(models.Model):
    groupID = models.ForeignKey(GroupDescription,on_delete=models.CASCADE)  
    userID = models.IntegerField(max_length=30)
    paidFrequency = models.IntegerField(max_length=30)
    paidDate = models.DateField(max_length=30)

class InvitationDetails(models.Model):
    groupID = models.IntegerField(max_length=30)  
    emailID = models.IntegerField(max_length=30)
    isInvite=models.IntegerField(max_length=30) 

class UserRating(models.Model):
    userID = models.IntegerField(max_length=30)
    userPoint = models.IntegerField(max_length=30)    
   
   
   
