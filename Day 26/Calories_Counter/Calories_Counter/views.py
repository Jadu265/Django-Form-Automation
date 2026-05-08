
from django.shortcuts import render,redirect
from datetime import date
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from Calories_Counter.forms import *
from Calories_Counter.models import *
# Create your views here.

def Register_page(request):
    if request.method == 'POST':
        form_data=RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login_page')
    
    form_data=RegistrationForm()
    context={
        'form_data':form_data,
        'form_title':'Registration Form',
        'form_btn':'Register'
    }
    
    return render (request, 'master/base-form.html', context)

def login_page(request):
    if request.method == 'POST':
        form_data=LoginFOrm(request, request.POST)
        if form_data.is_valid():
            user=form_data.get_user()
            login(request,user )
            messages.success(request, 'Login successful.')
            return redirect('Doashboard_page')
    
    form_data=LoginFOrm()
    context={
        'form_data':form_data,
        'form_title':'Login Form',
        'form_btn':'Login'
    }
    
    return render (request, 'master/base-form.html', context)

@login_required
def logout_page(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('login_page')

@login_required
def Doashboard_page(request):
    current_user=request.user
    try:
        bmr=round(request.user.User_Basic_Info.bmr, 2)
    except BasicInfoModel.DoesNotExist:
        bmr=0
        
    today=date.today()
    
    total_consumed_data=ConsumeCalories.objects.filter(
        Consumed_by=current_user,
        created_at=today
    ).aggregate(total=Sum('calories'))
    print(total_consumed_data)
    
    total_consumed = total_consumed_data['total'] or 0
    Less_or_More=round(bmr-total_consumed, 2)
    
    context={
        'Required_calories':bmr,
        'Consumed_calories':total_consumed,
        'Less_or_More':Less_or_More
    }
    
    return render (request,'Doashboard.html',context)

@login_required
def Profile_page(request):
    return render (request,'Profile.html')

def Update_profile(request):
    try:
     current_user=request.user.User_Basic_Info  
    except BasicInfoModel.DoesNotExist:
     current_user=None 
    if request.method == 'POST':
        form_data=ProfileUpdateForm(request.POST, instance=current_user)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.user=request.user
            weight=data.weight
            height=data.height
            age=data.age
            if data.gender == 'Male':
                #BMR= 66.47+(13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)
                bmr= 66.47+(13.75 * weight ) + (5.003 * height) - (6.755 * age)
            else:
                #BMR= 655.1+(9.563 x weight in kg) + (1.850 x height in cm) - (4.676 x age in years)
                bmr= 655.1+(9.563 * weight ) + (1.850 * height) - (4.676 * age) 
            data.bmr=bmr
            data.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('Profile_page')
    
    form_data=ProfileUpdateForm(instance=current_user)
    context={
        'form_data':form_data,
        'form_title':'Update Profile',
        'form_btn':'Update'
    }
    return render (request, 'master/base-form.html',context)

def consume_calories_list(request):
    consume_data=ConsumeCalories.objects.filter(Consumed_by=request.user)
    context={
        'consume_data':consume_data
    }

    return render (request,'Calories-list.html',context)

def add_calories(request):
    if request.method == 'POST':
        form_data=ConsumeCaloriesForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.Consumed_by=request.user
            data.save()
            messages.success(request, 'Calories added successfully.')
            return redirect('consume_calories_list')
    
    form_data=ConsumeCaloriesForm()
    context={
        'form_data':form_data,
        'form_title':'Add Calories',
        'form_btn':'Add Data'
    }
    
    return render(request,'master/base-form.html',context)

def update_calories(request,id):
    try:
        data=ConsumeCalories.objects.get(id=id)
    except ConsumeCalories.DoesNotExist:
        data=0
    if request.method == 'POST':
        form_data=ConsumeCaloriesForm(request.POST, instance=data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.Consumed_by=request.user
            data.save()
            messages.success(request, 'Calories updated successfully.')
            return redirect('consume_calories_list')
    
    form_data=ConsumeCaloriesForm(instance=data)
    context={
        'form_data':form_data,
        'form_title':'Update Calories',
        'form_btn':'Update Data'
    }
    
    return render(request,'master/base-form.html',context)

def delete_calories(request,id):
    try:
        data=ConsumeCalories.objects.get(id=id)
    except ConsumeCalories.DoesNotExist:
        data=0
    data.delete()
    messages.success(request, 'Calories deleted successfully.') 
    return redirect('consume_calories_list')
    