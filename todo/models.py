from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)  # The name or description of the task
    completed = models.BooleanField(default=False)  # True if the task is done
    created_at = models.DateTimeField(auto_now_add=True)  # When the task was created
    #due_date = models.DateField(null=True, blank=True)  # Optional due date
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link task to a user
    list = models.ForeignKey('List', on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)  # Link task to a list (optional)
    
    def __str__(self):
        return self.title  # Shows the task title in admin and shell

# Model for categorizing tasks into lists
class List(models.Model):
    list_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def total_tasks(self):
        return self.tasks.count()

    @property
    def completed_tasks(self):
        return self.tasks.filter(completed=True).count()

    def __str__(self):
        return self.list_name