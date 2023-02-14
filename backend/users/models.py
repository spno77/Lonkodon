from django.db import models

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.contrib.auth import get_user_model

#User manager
class UserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if username is None:
			raise TypeError('Users must have a username.')
		if email is None:
			raise TypeError('Users must have an email address.')

		user = self.model(username=username, email=self.normalize_email(email))
		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, username, email, password):

		if password is None:
			raise TypeError('Superusers must have a password.')
		user = self.create_user(username, email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()

		return user

class User(AbstractBaseUser,PermissionMixin):

    username    = models.CharField(db_index=True,unique=True,null=False,max_length=20)
    email       = models.EmailField(db_index=True,unique=True,max_length=50)
    is_staff    = models.BooleanField(default=False)
    firstname   = models.CharField(max_length=50,null=False)
    lastname    = models.CharField(max_length=50,null=False)
    phone       = models.CharField(max_length=20,null=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)

    
    def __str__(self):
        return self.username
    





