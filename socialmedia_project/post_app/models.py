from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core import validators
from django.core.validators import *
import os

# Create your models here.

def post_directory(self,filename):
    return "user{0}/post/{1}".format(self.author.username,filename)

class Post(models.Model):
    description = models.TextField(max_length=50, validators =[validators.MaxLengthValidator(50)])
    post_image = models.FileField(upload_to = post_directory)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,blank = True , related_name = 'likes')
    dislikes = models.ManyToManyField(User,blank = True , related_name = 'dislikes')

    def __str__(self):
        return self.author.username + " " + str(self.created_on)


    def extension(self):
        name, extension = os.path.splitext(self.post_image.name)
        return extension

    