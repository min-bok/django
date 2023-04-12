from django.shortcuts import render
from django.http import HttpResponse

def projects(req):
    return render(req, "projects/projects.html")

def project(req, pk):
    return render(req, "projects/single-project.html")