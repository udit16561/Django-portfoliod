from django.db import models

class contact(models.Model):
    Name=models.CharField(max_length=50)
    Post=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    PhoneNo=models.IntegerField()
    Birthday=models.DateField(auto_now=False, auto_now_add=False)
    Location=models.CharField(max_length=50)
    Description=models.TextField(default="none")

    
    
# Create your models here.
