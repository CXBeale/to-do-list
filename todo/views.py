from django.shortcuts import render
from .models import Task

# Create your views here.
def home(request):
    return render(request, 'todo/home.html')

def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    return render(request, 'todo/task_list.html', {'tasks': tasks})

