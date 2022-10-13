from django.urls import path
from .views import show_todolist, login_user, register, create_task, logout_user, delete_task, status_task, show_todolist_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', create_task, name='create_task'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('delete_task/<int:id>', delete_task, name='delete'),
    path('status_task/<int:id>', status_task, name='status_task'),
    path('json/', show_todolist_json, name='show_todolist_json'),
]