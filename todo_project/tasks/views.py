from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from tasks.forms import *

# Create your views here.
def Register_page(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if password==confirmpassword:
            CustomInfoModel.objects.create_user(
            fullname=fullname,
            username=username,
            email=email,
            password=password
            )
            return redirect('login-page')
    return render (request, 'register.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username , password=password)
    
        if user:
            login(request, user)
            return redirect('home_page')
        else:
            print("Invalid Credential")
    
    return render(request, 'login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect('login-page')

@login_required
def home_page(request):
    
    return render(request, 'home_page.html')

def task_page(request):
    task_data=TaskModel.objects.all()
    context={
        'task_data':task_data
    }
    return render(request, 'task-list.html',context)

def add_task(request):
    if request.method=='POST':
        form_data=taskform(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by=request.user
            data.save()
            return redirect('task_list')
    form_data=taskform()
    context={
        'form_data':form_data,
        'title':'Add Task Form',
        'btn_name':'Add Task',
    } 
    return render(request, 'master/base-form.html',context)

def update_task(request,id):
    task_data=get_object_or_404(TaskModel, id=id)
    if request.method=='POST':
        form_data=taskform(request.POST,instance=task_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by=request.user
            data.save()
            return redirect('task_list')
    form_data=taskform(instance=task_data)
    context={
        'form_data':form_data,
        'title':'Update Task Form',
        'btn_name':'Update Task',
    } 
    return render(request, 'master/base-form.html',context)

def delete_task(request,id):
    get_object_or_404(TaskModel,id=id).delete()
    return redirect('task_list')

def view_page(request, id):
    task_data=get_object_or_404(TaskModel,id=id)
    context={
        'task_data':task_data
    }

    return render(request,'card-details.html',context)
    
