from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)  # The name or description of the task
    completed = models.BooleanField(default=False)  # True if the task is done
    created_at = models.DateTimeField(auto_now_add=True)  # When the task was created
    due_date = models.DateField(null=True, blank=True)  # Optional due date

    def __str__(self):
        return self.title  # Shows the task title in admin and shell