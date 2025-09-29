from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.

# View for the home page
def home(request):
    return render(request, 'todo/home.html')

# View to list all tasks
def task_list(request):
    tasks = Task.objects.all()  # Get all tasks from the database
    return render(request, 'todo/task_list.html', {'tasks': tasks})

# New view to handle adding a task
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})