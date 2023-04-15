from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(req):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(req, "projects/projects.html", context)

def project(req, pk):
    projectObj = Project.objects.get(id=pk)
    return render(req, "projects/single-project.html", {'project':projectObj})

def createProject(req):
    form = ProjectForm()

    if req.method == "POST":
        form = ProjectForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(req, "projects/project_form.html", context)

def updateProject(req, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if req.method == "POST":
        form = ProjectForm(req.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(req, "projects/project_form.html", context)