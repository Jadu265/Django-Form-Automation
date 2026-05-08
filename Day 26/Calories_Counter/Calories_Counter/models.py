from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'

class BasicInfoModel(models.Model):
    GENDER_TYPES=[
        ('Male','MALE'),
        ('Female','Female')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, related_name='User_Basic_Info')
    name= models.CharField(max_length=100 , null=True)
    age = models.PositiveBigIntegerField(null=True)
    gender= models.CharField(max_length=10, choices=GENDER_TYPES, null=True)
    weight = models.FloatField  (null=True)
    height = models.FloatField  (null=True) 
    bmr= models.FloatField(null=True)
    
    def __str__(self):
        return f'{self.name}'

class ConsumeCalories(models.Model):
    
    item_name=models.CharField(max_length=200, null=True)
    calories=models.FloatField(null=True)
    created_at=models.DateField(auto_now_add=True, null=True)
    Consumed_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='User_Calories')
    
    def __str__(self):
        return f'{self.item_name} - {self.Consumed_by.username}'
    