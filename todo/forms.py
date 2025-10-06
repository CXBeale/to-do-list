from django import forms
from .models import Task, List

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'list']  # exclude 'completed'