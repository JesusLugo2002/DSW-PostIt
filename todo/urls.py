from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('pending_tasks', views.pending_tasks, name='pending_tasks'),
    path('done_tasks', views.done_tasks, name='done_tasks'),
    path('tasks/<task_slug>/', views.task_detail, name="task_detail")
]
