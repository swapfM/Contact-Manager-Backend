from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('name'), max_length = 100)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), unique = True, max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email']


    objects = CustomUserManager()


class Contact(models.Model):
    owner = models.ForeignKey('User', related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    phone = models.BigIntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name