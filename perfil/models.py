from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from blog.models import Post

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email, password):
        user = self.create_user(
            email = email,
            password=password,
        )
        user.is_admin = False,
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password):
        user = self.create_user(
            username,
            email,
            password
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser): 
    ...
    objects = UserManager()

class Usuario(AbstractUser):
    foto = models.ImageField(
        verbose_name='foto de perfil',
        height_field=None, 
        width_field=None, 
        max_length=200,
        blank = True, 
        null = True
    )
    username = models.CharField(
        verbose_name='username',
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='Correo electronico',
        unique=True,
    )
    post_favoritos = models.ManyToManyField(
        Post,
        null=True,
        blank=True,
    )
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
