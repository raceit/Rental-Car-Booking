from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30,default='')
    department = models.CharField(max_length=30,default='')
    phone = models.IntegerField(default=0)
    

class Booking(models.Model):
    sapno = models.IntegerField(default=0)
    your_name = models.CharField(max_length=300)
    mobileNumber = models.IntegerField(default=0)
    guestsapno=models.IntegerField(default=0)
    email=models.CharField(max_length=255, validators=[EmailValidator])
    #time = models.TimeField(default=timezone.now)
    time = models.TimeField(blank=True, null=True)
    #mobileNumber = PhoneNumberField(null=False, blank=False, unique=True)
    #mobileNumber=models.IntegerField(default=0)
    #mobilenumber=models.CharField(max_length=300,default="0")    
