from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
     'id' : '1',
     'title': '쇼핑몰', 
     'description': '상품판매를 위한 웹사이트입니다.'
    },
    {
     'id' : '2',
     'title': '포트폴리오', 
     'description': '포트폴리오 웹사이트입니다.'
    },
    {
     'id' : '3',
     'title': '학습사이트', 
     'description': '학습을 위한 웹사이트입니다.'
    },
]

def projects(req):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(req, "projects/projects.html", context)

def project(req, pk):
    projectObj = Project.objects.get(id=pk)
    return render(req, "projects/single-project.html", {'project':projectObj})