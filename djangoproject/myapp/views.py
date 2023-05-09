from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project, Task

from .forms import CreateNewTask, CreateNewProject


# Create your views here.
def index(request):
    title = "Welcome to the main page"
    return render(
        request,
        "index.html",
        {
            "title": title,
        },
    )


def about(request):
    username = "Matthews"
    return render(
        request,
        "about.html",
        {
            "username": username,
        },
    )


# complemento generico
def helloWorld(request, username):
    return HttpResponse(
        "<h1>Hola, bienvenido %s, es hora de que trabajes :3 </h1>" % username
    )


# projects
def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "project/projects.html", {"projects": projects})


# tareas
def tasks(request):
    # task= Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, "task/tasks.html", {"tasks": tasks})


# creacion de las tareas
def create_task(request):
    if request.method == "GET":
        return render(request, "task/create_task.html", {"form": CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=2,
        )

        return redirect("tasks")


# creacion de las proyectos


def create_project(request):
    if request.method == "GET":
        return render(
            request, "project/create_project.html", 
            {"form": CreateNewProject()})
        
    else:
        project=Project.objects.create( name=request.POST["name"])
        return redirect('projects')
        
def project_detail(request, id):
 
    project=get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, "project/detail.html", {
        'project': project,
        'tasks': tasks,
    })
