from django.contrib.auth.models import (
    BaseUserManager
)

from .models import *

class UserManager(BaseUserManager):
    def create_user(self, email, mobile_number, user_type, password=None, is_staff=False, is_superuser=False, is_active=False):

        print('creating a non-active, non-superuser and non-staff user')

        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        if not user_type:
            raise ValueError("User must have a user type")
        if not mobile_number:
            raise ValueError("User must have a mobile number")              
        user_obj = self.model(
            email = self.normalize_email(email)
        )

        user_obj.set_password(password)  # set or change password
        user_obj.staff = is_staff
        user_obj.superuser = is_superuser
        user_obj.active = is_active
        user_obj.mobile_number = mobile_number
        user_obj.user_type = user_type
        
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, mobile_number, user_type, password=None):

        print('creating a staff user')

        user = self.create_user(
            email=email,
            password=password,
            mobile_number = mobile_number,
            user_type = user_type,
            is_staff=True,
            is_active=True
        )
        return user

    def create_superuser(self, email, mobile_number, user_type, password=None):

        print('creating a super user')

        user = self.create_user(
            email=email,
            password=password,
            mobile_number = mobile_number,
            user_type = user_type,
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        return user

    def get_user_by_user_type(self, user_type):
        return self.get_queryset().filter(user_type=user_type)

    def get_user_by_email(self, email):
        return self.get_queryset().filter(email=email)    


class StaffManager(models.Manager):

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = email_name + '@' + domain_part.lower()
        return email


    def create_staff(self, email, mobile_number, password=None):

        print('creating a staff member')

        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        if not mobile_number:
            raise ValueError("User must have a mobile number")              
        staff_obj = self.model(
            email = self.normalize_email(email)
        )

        staff_obj.set_password(password)  # set or change password
        staff_obj.mobile_number = mobile_number
        staff_obj.is_staff=True
        staff_obj.is_active=True

        staff_obj.save(using=self._db)
        return staff_obj        