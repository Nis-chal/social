from django.db import models
from django.contrib.auth.models import User
from post_app.models import Post
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)

    def __str__(self):
        return self.author.username + " " + str(self.created_on) + "comment"