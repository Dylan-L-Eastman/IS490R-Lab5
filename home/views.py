from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! You’re at the home index. CodeDeploy working.")

# Create your views here.
