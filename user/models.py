from cgi import print_form
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, Group, Permission)
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (check_password, is_password_usable, make_password,)
from django.utils.crypto import get_random_string, salted_hmac
from django.core.validators import RegexValidator
from phonenumbers import is_valid_number_for_region

from .managers import UserManager

from . import utils as systemutils
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
#from phone_field import PhoneField

from .utils import USER_TYPE_CHOICES

from django.contrib.auth import get_user_model
# from user.managers import StaffManager

         

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.utils.crypto import get_random_string, salted_hmac

from .managers import UserManager

from .utils import *


import datetime
import hashlib
import os

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.loader import render_to_string

from phonenumber_field.modelfields import PhoneNumberField
# from sendsms.message import SmsMessage  

class RateGroupManager(models.Manager):
    def get_queryset(self):
        return RateGroupQuerySet(self.model, using=self._db)

    def get_rate_group(self):
        return self.get_queryset().get_rate_group()

class RateGroupQuerySet(models.query.QuerySet):

    def get_rate_group(self):
        user_qs = RateGroup.objects.all()
        return user_qs


class RateGroup(models.Model):

    rate_group_id = models.AutoField(primary_key=True)
    rate_group_name = models.CharField(max_length=255, help_text=" Name of a rate card group")
   # objects = RateGroupManager()

    def __str__(self):
        return self.rate_group_name

    class Meta:
        db_table = 'rate_group'


class BaseUser(models.Model):

    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255,null=True,blank=True)
    date_of_birth = models.DateField(blank=True, null=True,help_text=('date format: yyyy-mm-dd    ex:2018-11-15') )
    mobile_number = models.CharField(max_length=30)
    alternate_number = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(max_length= 100, blank=True, null=True, choices=systemutils.USER_GENDER_CHOICES)
    # address = models.ForeignKey(GeneralAddress, blank=True, null=True, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False, help_text=('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(default=False,
                                    help_text=(
                                        'Designates whether this user should be treated as active. '
                                        'Unselect this instead of deleting accounts.'
                                    ),
                                )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    registered_by = models.EmailField(max_length=255,null=True,blank=True)

    _password = None

    class Meta:
        abstract = True

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._password is not None:
            password_validation.password_changed(self._password, self)
            self._password = None    

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        # Set a value that will never be a valid hash
        self.password = make_password(None)

    def has_usable_password(self):
        """
        Return False if set_unusable_password() has been called for this user.
        """
        return is_password_usable(self.password)

    def get_session_auth_hash(self):
        """
        Return an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(key_salt, self.password).hexdigest()    

# Custom User with extended group permissions functionality
class User(AbstractBaseUser, PermissionsMixin):

    """
    Email, password, user type, mobile number are required. Other fields are optional.
    """

    user_id = models.AutoField(primary_key=True)
    
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=255)
   # mobile_number = models.CharField(max_length=30)
    phone_regex = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 14 digits allowed.")
    mobile_number = models.CharField(validators =[phone_regex],blank=False, max_length=11, unique = True)
    alternate_number = models.CharField(max_length=30, blank=True, null=True)
    active = models.BooleanField(default=False,
                                    help_text=(
                                        'Designates whether this user should be treated as active. '
                                        'Unselect this instead of deleting accounts.'
                                    ),
                                ) # can login
    staff = models.BooleanField(default=False, help_text=('Designates whether the user can log into this admin site.')) # staff user non superuser
    superuser = models.BooleanField(default=False) # superuser

    # _groups = models.ManyToManyField(Group, blank=True)
    # _user_permissions = models.ManyToManyField(
    #     Permission, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    user_type = models.CharField(max_length=255, choices=systemutils.USER_TYPE_CHOICES)

    date_of_birth = models.DateField(blank=True, null=True, help_text=('date format: yyyy-mm-dd    ex:2018-11-15') )
    #aadhar_number = models.CharField(max_length=20, blank=True, null=True)
    #GSTIN = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length= 100, blank=True, null=True, choices=systemutils.USER_GENDER_CHOICES)
    
    USERNAME_FIELD = 'email' # username

    REQUIRED_FIELDS = ['user_type', 'mobile_number']

    objects = UserManager()

    class Meta:
        db_table = 'user'   

    def __str__(self):
        return self.get_short_name

    @property
    def full_name(self):
        "Returns the person's full name."
        if self.middle_name is None and self.last_name is not None:
            return '%s %s' % (self.first_name, self.last_name)
        elif self.middle_name is not None and self.last_name is None:
            return '%s %s' % (self.first_name, self.middle_name)
        elif self.middle_name is not None and self.last_name is not None:
            return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

        return self.first_name

    @property
    def get_short_name(self):
        "Returns the person's short name to show after welcome on UI."
        if self.full_name:
            return self.full_name 
        elif self.first_name:
            return self.first_name  
        return self.email    

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.superuser

    

    def save(self, *args, **kwargs):
        print("Saving new user for admin panel : "+ str(self))
        super(User, self).save(*args, **kwargs)




