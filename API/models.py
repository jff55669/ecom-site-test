from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        email = self.normalize_email(email)
        new_user = self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('is_super user is false'))
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('is_staff is false'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('is_active is false'))
        return self.create_user(email,password,**extra_fields)
    
    


class User(AbstractUser):
    username = models.CharField(max_length=30, unique= True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()


# class User(models.Model):
#     username = models.CharField(max_length=200)
#     email = models.EmailField()
#     number = PhoneNumberField()
    
#     def __str__(self):
#         return self.username
 
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('delivered','Delivered'),
        ('canceled','Canceled'),
        
    ]
    
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name} by {self.user.username}"
    
