from django.urls import path
from todolist.views import show_todolist, login_user, register, create_task, logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create-task'),
    path('logout/', logout_user, name='logout'),
]