from django.db import models

# Create your models here.

class User(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(null=True,blank=True,max_length=100)
    department=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    date=models.DateField()
    salary=models.IntegerField()
    image=models.FileField(null=True,blank=True,upload_to='media')
