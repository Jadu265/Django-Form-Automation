from django import forms
from tasks.models import *


class taskform(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'
        exclude=['created_by']
        
        widgets={
            'due_date':forms.DateInput(attrs={'type':'date'})
        }