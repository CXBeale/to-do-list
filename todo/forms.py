from django import forms
from .models import Task, List

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'list']  # exclude 'completed'

    # override init to filter list choices by user
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['list'].queryset = List.objects.filter(user=user)