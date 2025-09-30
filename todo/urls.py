from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # '' means the root of /todo/
    path('tasks/', views.task_list, name='task_list'),  # /todo/tasks/ will show the list of tasks
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]