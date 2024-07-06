from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, unique=True, default=None, null=False)
    last_name = models.CharField(max_length=50, null=False, default=None)
    password = models.CharField(max_length=50, unique=True, default=None, null=False, blank=False)
    image_profile = models.ImageField(upload_to='profile/', null=True, blank=True)
    bio = models.TextField()
    type_user = models.CharField(max_length=50, default=None, null=False, blank=False)
    
    def __str__(self):
        return self.username

