from django.shortcuts import render

from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'todo/home.html', dict(tasks=tasks))

def pending_tasks(request):
    tasks = Task.objects.filter(done=False)
    return render(request, 'todo/home.html', dict(tasks=tasks))

def done_tasks(request):
    tasks = Task.objects.filter(done=True)
    return render(request, 'todo/home.html', dict(tasks=tasks))

def task_detail(request, task_slug):
    task = Task.objects.get(slug=task_slug)
    return render(request, 'todo/task/task_detail.html', dict(task=task))