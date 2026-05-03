from django.urls import path
from tasks.views import *

urlpatterns = [
    path('',Register_page,name='register-page'),
    path('login/',login_page,name='login-page'),
    path('logout/',logout_page,name='logout_page'),
    path('home-page/',home_page,name='home_page'),
    #path('TaskPage/',task_page,name='task_list'),
   
    path('profile/',profile_page,name='profile_page'),
    path('update_profile/',profile_update,name='update_profile'),
    path('product-list/',product_page,name='product_list'),
    path('add-product/',add_product,name='add_product'),
    
]
