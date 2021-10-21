from django.db import models

# Create your models here.
class User(models.Model):
    
    name=models.CharField( max_length=40)
    email=models.CharField(max_length=50)
    phoneNumber=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
    date=models.DateField()
    
    
    

