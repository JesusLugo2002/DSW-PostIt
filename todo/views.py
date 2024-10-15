from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Task
from .forms import AddTaskForm

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

def add_task(request):
    if request.method == "GET":
        form = AddTaskForm()
    else:
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.title)
            task.save()
            return redirect('todo:home')
        
    return render(request, 'todo/task/add.html', dict(form=form))