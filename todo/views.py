from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task, List
from .forms_list import ListForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# View for the home page
def home(request):
    return render(request, 'todo/home.html')

# View to list all tasks
@login_required
def task_list(request):
    lists = List.objects.filter(user=request.user).prefetch_related('tasks')
    return render(request, 'todo/task_list.html', {'lists': lists})

# New view to handle adding a task (specific to a user)
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)  # Don’t save to DB yet
            task.user = request.user        # Assign the current user
            # If no list is selected, assign to 'General' list
            if not task.list:
                from .models import List
                general_list, created = List.objects.get_or_create(
                    user=request.user,
                    list_name='General',
                    defaults={'description': 'Default list for uncategorized tasks.'}
                )
                task.list = general_list
            task.save()                     # Now save to DB
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'todo/add_task.html', {'form': form})

# New view to mark a task as complete
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')

# New view to delete a task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

# New view to edit a task
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})

# View to toggle the completion status of a task
@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


# List management views
@login_required
def list_overview(request):
    lists = List.objects.filter(user=request.user)
    return render(request, 'todo/list_overview.html', {'lists': lists})

@login_required
def create_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            return redirect('list_overview')
    else:
        form = ListForm()
    return render(request, 'todo/create_list.html', {'form': form})

@login_required
def edit_list(request, list_id):
    list_obj = get_object_or_404(List, id=list_id, user=request.user)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=list_obj)
        if form.is_valid():
            form.save()
            return redirect('list_overview')
    else:
        form = ListForm(instance=list_obj)
    return render(request, 'todo/edit_list.html', {'form': form, 'list': list_obj})

@login_required
def delete_list(request, list_id):
    list_obj = get_object_or_404(List, id=list_id, user=request.user)
    if request.method == 'POST':
        list_obj.delete()
        return redirect('list_overview')
    return render(request, 'todo/delete_list.html', {'list': list_obj})



