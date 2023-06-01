from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):
    name=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    department=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    is_admin=models.BooleanField(default=False)    
    is_student=models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)