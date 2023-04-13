from django.shortcuts import render
from django.http import HttpResponse

def projects(req):
    page = "projects"
    number = 9
    context = {'page': page, "number":number}
    return render(req, "projects/projects.html", context)

def project(req, pk):
    return render(req, "projects/single-project.html")