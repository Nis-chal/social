from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core import validators
from django.core.validators import *

# Create your models here.

def profile_pic_directory(self,filename):
    return "user{0}/profile_pic/{1}".format(self.user.username,filename)

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile', validators = [validators.MaxLengthValidator(8)])
    name = models.CharField(max_length=30,blank=True,null=True)  
    portfolio_site = models.URLField(blank=True,validators =[validators.MaxLengthValidator(200)])
    profile_pic = models.ImageField(upload_to =profile_pic_directory,blank = True,default = 'def.jpg')
    bio = models.CharField(max_length=50 ,validators =[validators.MaxLengthValidator(50)])
    followers = models.ManyToManyField(User,blank=True,related_name='followers',default=[0])
    following = models.ManyToManyField(User,blank=True ,related_name ='following',default=[0])
    birth_date = models.DateField(null=True,blank=True)
    location =models.CharField(max_length=100,blank=True,null=True)
    
    def __str__ (self):
        return self.user.username
