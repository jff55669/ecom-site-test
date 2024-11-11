from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    number = PhoneNumberField()
    
    def __str__(self):
        return self.username
 
    
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
    
