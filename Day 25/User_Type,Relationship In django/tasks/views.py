from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from tasks.forms import *
from django.contrib import messages

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



def view_page(request, id):
    task_data=get_object_or_404(TaskModel,id=id)
    context={
        'task_data':task_data
    }

    return render(request,'card-details.html',context)

def profile_page(request):
    
    return render(request,'profile.html')
    
def profile_update(request):
    
    try:
        model_data=request.user.user_profile
    except profileModel.DoesNotExist:
        model_data=None
        
    if request.method=='POST': 
        form_data=updateProfile(request.POST,request.FILES,instance=model_data)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.user=request.user
            data.save()
            return redirect ('profile_page')
        
    form_data=updateProfile(instance=model_data)
    context={
        'form_data':form_data,
        'title':'Update Profile Info',
        'btn_name': 'Update'
    }
    
    return render( request,'master/base-form.html',context)
    
def product_page(request):
    product_data=productModel.objects.filter(created_by=request.user)
    context={
        'product_data':product_data,
    }
    return render(request,'product-list.html',context)

def add_product(request):
    if request.method=='POST':
        form_data=ProductForm(request.POST)
        if form_data.is_valid():
            data=form_data.save(commit=False)
            data.created_by=request.user
            form_data.total_amount=form_data.price * form_data.qty
            data.save()
            return redirect ('product_list')
    form_data=ProductForm()
    context={
        'form_data':form_data,
        'title':'Add Product',
        'btn_name': 'Update'
    }
    
    return render( request,'master/base-form.html',context)