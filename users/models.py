from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField('email address', unique=True)
	is_staff = models.BooleanField(default=False) # True if the user is allowed to have access to the admin site.
	is_active = models.BooleanField(default=True)
	date_joined = models.DateTimeField(default=timezone.now)
	first_name = models.CharField(max_length=150, blank=True)
	last_name = models.CharField(max_length=150, blank=True)
	nickname = models.CharField(max_length=50, blank=True)
	# user_category = models. ForeignKey

	USERNAME_FIELD = 'email'
	REQUIDER_FIELDS = []

	objects = CustomUserManager()

	def __str__(self):
		return self.email

