from django.shortcuts import render

from .models import Task

# Create your views here.
def tasks_panel(request):
    tasks = Task.objects.all()
    return render(request, 'todo/tasks_panel.html', dict(tasks=tasks))

def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'todo/task/task_detail.html', dict(task=task))