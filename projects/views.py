from django.shortcuts import render
from django.http import HttpResponse

def projects(req):
    return HttpResponse("here is our products!")

def project(req, pk):
    return HttpResponse("single project" + pk)
