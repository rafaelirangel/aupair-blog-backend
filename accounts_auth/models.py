from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

##Customizing user 
##This is where you can manage things
class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must enter an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to have is_staff being True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have is_superuser being True')
        

        return self.create_user(email=email, password=password, **extra_fields)
        
        
    
##User account using Abstract and Permissions to personalize the user  
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
