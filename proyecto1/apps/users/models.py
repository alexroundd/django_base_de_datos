from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    USER_CHOICES = (
        ('administrator', 'ADMINISTRATOR'),
        ('editor', 'EDITOR'),
        ('viewer', 'VIEWER'),
    )

    email = models.EmailField('email', unique=True)
    usertype = models.CharField(max_length=20, choices=USER_CHOICES, default='viewer')
    image = models.ImageField(upload_to='media', blank=True, null=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')

    def __str__(self):
        return self.email

    objects = UserManager()
