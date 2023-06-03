from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def todo(Request):
    returnobject = HttpResponse('hello todi')
    return returnobject
