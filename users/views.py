from django.shortcuts import render

def profiles(req):
    return render(req, 'users/profiles.html')
