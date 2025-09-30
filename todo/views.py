from django.shortcuts import render, redirect, get_object_or_404
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

# New view to mark a task as complete
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# New view to delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')