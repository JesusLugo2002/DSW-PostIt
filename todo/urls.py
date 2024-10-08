from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.tasks_panel, name='tasks_panel'),
    path('tasks/<task_slug>/', views.task_detail, name="task_detail")
]
