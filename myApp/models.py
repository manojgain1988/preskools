from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customUser(AbstractUser):
    
    USER=(
        ('1','Admin'),
        ('2','Teacher'),
        ('3','Student'),
    )
    user_type = models.CharField(choices=USER, max_length=100,null=True)
    profile_pic = models.ImageField(upload_to='media/profile_pic',null=True)
    
    def __str__(self):
        return self.username
    