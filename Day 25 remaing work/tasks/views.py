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
        user_type=request.POST.get('user_type')
        
        if password==confirmpassword:
            CustomInfoModel.objects.create_user(
            fullname=fullname,
            username=username,
            email=email,
            password=password,
            user_type=user_type
            )
            messages.success(request,'Account created Successfully')
            return redirect('login-page')
        else:
            messages.success(request,'Password Does not Match')
            return redirect('register-page')
    return render (request, 'register.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username , password=password)
    
        if user:
            login(request, user)
            messages.success(request,'Login Successful')
            return redirect('home_page')
        else:
            messages.error(request, 'Invalid credential, please try again')
    
    return render(request, 'login.html')

@login_required
def logout_page(request):
    logout(request)
    messages.success(request,'Logout Successful')
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
            messages.success(request,'Update Successful')
            return redirect ('profile_page')
        
    form_data=updateProfile(instance=model_data)
    context={
        'form_data':form_data,
        'title':'Update Profile Info',
        'btn_name': 'Update'
    }
    
    return render( request,'master/base-form.html',context)
    
def product_page(request):
    current_user=request.user
    if current_user.user_type =='Buyer':
        product_data=productModel.objects.all()
    else:
        product_data=productModel.objects.filter(created_by=request.user)
    context={
        'product_data':product_data,
    }
    return render(request,'product-list.html',context)

def add_product(request):
    if request.method=='POST':
        form_data=ProductForm(request.POST)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.created_by=request.user
            form_data.total_amount=form_data.price * form_data.qty
            form_data.save()
            messages.success(request,'Product added Successfully')
            return redirect ('product_list')
    form_data=ProductForm()
    context={
        'form_data':form_data,
        'title':'Add Product',
        'btn_name': 'Update'
    }
    
    return render( request,'master/base-form.html',context)

def update_product(request,id):
    try:
        product_data=productModel.objects.get(id=id)
    except productModel.DoesNotExist:
        product_data=None
    if request.method=='POST':
        form_data=ProductForm(request.POST, instance=product_data)
        if form_data.is_valid():
            form_data=form_data.save(commit=False)
            form_data.created_by=request.user
            form_data.total_amount=form_data.price * form_data.qty
            form_data.save()
            messages.success(request,'Product Updated Successfully')
            return redirect ('product_list')
    form_data=ProductForm(instance=product_data)
    context={
        'form_data':form_data,
        'title':'Update Product',
        'btn_name': 'Update'
    }
    
    return render( request,'master/base-form.html',context)

def Productview_page(request, id):
    product_data=get_object_or_404(productModel,id=id)
    context={
        'product_data':product_data
    }

    return render(request,'product-view.html',context)
    
def Delete_product(request, id):
    product_data=get_object_or_404(productModel,id=id)
    product_data.delete()
    messages.success(request,'Product Deleted Successfully')
    return redirect('product_list')