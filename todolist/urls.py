from django.urls import path

from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user 
from todolist.views import logout_user
from todolist.views import add_todo, change_is_finished, delete_task


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_todo/', add_todo, name='add_todo'),
    path('change_is_finished/<int:id>', change_is_finished, name='change_is_finished'),
    path('delete_task/<int:id>', delete_task, name='delete_task')
]