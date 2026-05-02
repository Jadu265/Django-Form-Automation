from django.urls import path
from tasks.views import *

urlpatterns = [
    path('',Register_page,name='register-page'),
    path('login/',login_page,name='login-page'),
    path('logout/',logout_page,name='logout_page'),
    path('home-page/',home_page,name='home_page'),
    path('TaskPage/',task_page,name='task_list'),
    path('add-task/',add_task,name='add_task'),
    path('update-task/<str:id>/',update_task,name='update_task'),
    path('delete-task/<str:id>/',delete_task,name='delete_task'),
    path('view-task/<str:id>/',view_page,name='view_task'),
]
