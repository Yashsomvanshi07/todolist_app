from django.urls import path
from .views import todolist, edit_task, delete_task, toggle_task

urlpatterns = [
    path('', todolist, name='todolist'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('toggle_task/<int:task_id>/', toggle_task, name='toggle_task'),  # Add this URL for toggling task completion
]
