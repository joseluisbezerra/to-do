from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('tasks/<int:id>', views.task_view, name='task-view'),
    path('newtask/', views.new_task, name='new-task'),
    path('edit/<int:id>', views.edit_task, name='edit-task'),
    path('chagestatus/<int:id>', views.change_status, name='change-status'),
    path('delete/<int:id>', views.delete_task, name='delete-task'),
]
