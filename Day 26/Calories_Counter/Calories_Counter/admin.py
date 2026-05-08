from django.contrib import admin
from Calories_Counter.models import *
# Register your models here.
admin.site.register([User, BasicInfoModel, ConsumeCalories])