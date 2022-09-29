from socket import fromshare
from django import forms
from todolist.models import Task

class AddToDo(forms.Form):
    class Meta:
        model = Task
        fields = ['title', 'description']