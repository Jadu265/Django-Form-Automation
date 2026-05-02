from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomInfoModel(AbstractUser):
    
    fullname=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f'{self.username}-{self.fullname}'
class  TaskModel(models.Model):
    #title, description, status(Pending, InProgress, Completed, Canceled), due_date, created_at,updated_at
    STATUS=[
        ('Pending','Pending'),
        ('InProgress','InProgress'),
        ('Completed','Completed'),
        ('Canceled','Canceled'),  
    ]
    title=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True)
    status=models.CharField(max_length=30, choices=STATUS, null=True)
    due_date=models.DateField(null=True)
    created_at=models.DateField(auto_now_add=True, null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    created_by=models.ForeignKey(CustomInfoModel,on_delete=models.CASCADE ,null=True)
    
    def __str__(self):
        return f'{self.title}'
    

    

    