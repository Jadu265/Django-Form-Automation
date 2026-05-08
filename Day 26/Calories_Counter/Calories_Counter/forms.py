from django import forms
from Calories_Counter.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginFOrm(AuthenticationForm):
    pass

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = BasicInfoModel
        fields = '__all__'
        exclude=['user','bmr']
        
class ConsumeCaloriesForm(forms.ModelForm):
    class Meta:
        model = ConsumeCalories
        fields = '__all__'
        exclude=['Consumed_by']
        