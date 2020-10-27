from django.db import models

# Create your models here.
class Employee(models.Model):
    
    employee_id = models.IntegerField()
    employee_name = models.TextField(max_length=30)
    address = models.TextField(max_length=100)
    dobDay = models.IntegerField()
    dobMon = models.TextField(max_length=10)
    dobYear = models.IntegerField()
    mobile_no = models.IntegerField()


