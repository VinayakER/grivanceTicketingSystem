from django.db import models
from account.models import User
# Create your models here.



class Grievance(models.Model):
    STATUS_OPTIONS=(
        (1,'New'),
        (2,'Open'),
        (3,'Resolved'),
        (4,'Closed'),
    )
    title=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.SmallIntegerField(choices=STATUS_OPTIONS,default=1)
