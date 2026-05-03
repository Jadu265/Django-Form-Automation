from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomInfoModel(AbstractUser):
    
    fullname=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f'{self.username}-{self.fullname}'
    
class profileModel(models.Model):
    user=models.OneToOneField(CustomInfoModel,on_delete=models.CASCADE,null=True,related_name='user_profile')
    address=models.TextField(null=True)
    contact=models.CharField(max_length=20,null=True)
    date_of_birth=models.DateField(null=True)
    image=models.ImageField(upload_to='media/profile_img', null=True)
    
    def __str__(self):
        return f'{self.user.fullname}'

class productModel(models.Model):
    name= models.CharField(max_length=50, null=True)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    qty=models.PositiveIntegerField(null=True)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    created_by=models.ForeignKey(
        CustomInfoModel,
        on_delete=models.CASCADE,
        null=True,
        related_name='user_product'
    )
created_at=models.DateTimeField(auto_now_add=True,null=True)
updated_at=models.DateTimeField(auto_now=True,null=True)
    

    