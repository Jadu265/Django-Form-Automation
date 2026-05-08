from django.urls import path
from Calories_Counter.views import *

urlpatterns = [
    path('', Register_page, name='Register_page'),
    path('login-page/', login_page, name='login_page'),
    path('logout-page/', logout_page, name='logout_page'),
    path('Doashboard/', Doashboard_page, name='Doashboard_page'),
    path('profile/', Profile_page, name='Profile_page'),
    path('Update-profile/', Update_profile, name='Update_profile'),
    path('consume-calories-list/', consume_calories_list, name='consume_calories_list'),
    path('add-calories/', add_calories, name='add_calories'),
    path('update-calories/<str:id>/', update_calories, name='update_calories'),
    path('delete-calories/<str:id>/', delete_calories, name='delete_calories'),

]