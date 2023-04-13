from django.shortcuts import render
from django.http import HttpResponse

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
    page = "projects"
    number = 9
    context = {'page': page, "number":number, 'projects': projectsList}
    return render(req, "projects/projects.html", context)

def project(req, pk):
    projectObj = None
    for i in projectsList:
        if i["id"] == pk:
            projectObj = i
    return render(req, "projects/single-project.html", {'project':projectObj})