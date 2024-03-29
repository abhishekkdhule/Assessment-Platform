from django.db import models

from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)

#User manager model
class UserManager(BaseUserManager):
    def create_user(self, email, password=None,**kwargs):
        if email is None:
            raise TypeError("User must have email")
        if password is None:
            raise TypeError("Password should not be none")
            
        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError("Password should not be none")
        if email is None:
            raise TypeError("User must have email")
        user=self.create_user(email,password)
        user.is_superuser=True
        user.is_staff=True
        user.set_password(password)
        user.save()
        return user

    
#Overriding Dafault User model
class User(AbstractBaseUser,PermissionsMixin):
    email=models.CharField(max_length=255,unique=True,db_index=True)
    name=models.CharField(max_length=255)
    is_recruiter=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELD=['email','name']
    objects=UserManager()

    def __str__(self):
        return self.email
        
  