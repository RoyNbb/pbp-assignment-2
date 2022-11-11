from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import HttpResponse, HttpResponseNotFound

from todolist.models import Task

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = Task.objects.filter(user = request.user)
    context = {
        'user' : request.user.username,
        'tasks': data,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolist.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user is not None:
                login(request, user) # melakukan login terlebih dahulu
                response = HttpResponseRedirect("/") # membuat response
                response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
                return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def add_todo(request):
    if request.method == 'POST': 
        user = request.user
        title = request.POST['title']
        desc = request.POST['description']
        task = Task.objects.create(user = user, title = title, description = desc)
        return redirect('todolist:show_todolist') # Redirect after POST
    
    return render(request, 'add_todo.html')


@login_required(login_url='/todolist/login/')
def change_is_finished(request, id):
    task = Task.objects.get(user=request.user, id = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task = Task.objects.get(user=request.user, id = id)
    task.delete()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    context = {
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, 'todolistajax.html', context)


# return all user tas in JSON format
def get_json(request):
    tasks = Task.objects.all()
    return HttpResponse(
        serializers.serialize("json", tasks),
        content_type='application/json'
    )

@login_required(login_url='/todolist/login/')
def add_todo_ajax(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        desc = request.POST.get("description")
        task = Task(user=user, title=title, description=desc)
        
        task.save()
        
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

# @login_required(login_url='/todolist/login/')
# def delete_task_ajax(request, id):
#     if request.method == "DELETE":
#         task = Task.objects.get(user=request.user)
#         task.delete()
#         return HttpResponse("Success Deleting Task")
#    return HttpResponseNotFound()

# @login_required(login_url='/todolist/login/')
# def change_is_finished_ajax(request, id):
#     if request.method == "POST":
#         task = Task.objects.get(user=request.user, id = id)
#         task.is_finished = not task.is_finished
#         task.save()
#         return HttpResponse("Success updating task")
#     return HttpResponseNotFound()

