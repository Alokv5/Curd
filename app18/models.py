from django.db import models

class Employee(models.Model):
    idno=models.IntegerField(unique=True)
    Name=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
    Salary=models.FloatField()
