from django import forms
from tasks.models import *


class updateProfile(forms.ModelForm):
    class Meta:
        model=profileModel
        fields='__all__'
        
        exclude=['user']
        
        widgets={
            'date_of_birth':forms.DateInput(attrs={'type':'date'})
        }
        
class ProductForm(forms.ModelForm):
    class Meta:
        model=productModel
        fields= '__all__'
        exclude=['total_amount','created_by']