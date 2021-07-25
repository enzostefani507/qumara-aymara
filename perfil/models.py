from django.contrib.auth.models import User
from django.db import models
from blog.models import Post 
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    favoritos = models.ManyToManyField(
        Post, 
        null=True, 
        blank=True,
    )