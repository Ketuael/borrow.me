from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)

    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True


