from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # '' means the root of /todo/
    path('add/', views.add_task, name='add_task'),
    path('add/<int:list_id>/', views.add_task, name='add_task_to_list'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),

    # List management
    path('lists/', views.list_overview, name='list_overview'),
    path('lists/create/', views.create_list, name='create_list'),
    path('lists/<int:list_id>/edit/', views.edit_list, name='edit_list'),
    path('lists/<int:list_id>/delete/', views.delete_list, name='delete_list'),
]