from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Task
from .forms import AddTaskForm
import requests

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, 'todo/home.html', dict(tasks=tasks))

def set_github(request):
    if request.method == "POST":
        github_user = request.POST.get('github-user')
        github_repo = request.POST.get('github-repo')
        if not github_user and github_repo:
            return HttpResponse("Username and repository name required!")
        else:
            return redirect('todo:github-issues', owner=github_user, repo=github_repo)
    return render(request, "todo/setting-github.html")
        

def github_issues(request, owner, repo):
    issues = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues").json()
    return render(request, "todo/github-issues.html", dict(issues=issues))

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