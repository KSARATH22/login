from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    x="<center><h1>Hello world</h1></center>"
    return HttpResponse(x)