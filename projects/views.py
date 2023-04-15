from django.shortcuts import render
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
    context = {'form':form}
    return render(req, "projects/project_form.html", context)