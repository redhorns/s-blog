from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    #other fields here

    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):  
          return "%s's profile" % self.name





