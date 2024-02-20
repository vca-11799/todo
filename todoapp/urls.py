from django.urls import path
from . import views

urlpatterns = [
    path('addtask/', views.addTask, name = 'addTask'),
    path('task_done/<int:pk>', views.taskDone, name = 'taskDone'),
    path('task_undone/<int:pk>', views.taskUnDone, name = 'taskUnDone'),
    path('edit_task/<int:pk>', views.editTask, name = 'editTask'),
    path('delete_task/<int:pk>', views.deleteTask, name = 'deleteTask')
]