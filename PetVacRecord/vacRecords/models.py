from django.db import models

# Create your models here.
class User(models.Model):
    
    name=models.CharField( max_length=40)
    email=models.CharField(max_length=50)
    phoneNumber=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
    date=models.DateField()
    
    def __str__(self):
        return self.name
    
    
class Pet(models.Model):

    name=models.CharField( max_length=50)
    animal=models.CharField( max_length=50)
    breed=models.CharField( max_length=50)
    birth=models.DateField()
    chipNumber=models.CharField( max_length=50)
    
    
class Health(models.Model):
    
    date=models.DateField()
    weight=models.SmallIntegerField("")
    height=models.CharField(max_length=5)

class Vaccine(models.Model):
    date=models.DateField()
    vaccine=models.CharField(max_length=50)
    nextDueDate=models.DateField()

class Medicines(models.Model):
    startDate=models.DateField()
    endDate=models.DateField()
    medicine=models.CharField(max_length=50)

class Checkup(models.Model):
    date=models.DateField()
    date=models.DateField()
    weight=models.CharField(max_length=5)
    height=models.CharField(max_length=5)
    checkupnotes=models.TextField("",null=True)
    prescription=models.CharField(max_length=50)
    nextCheckup=models.DateField()
    
    
