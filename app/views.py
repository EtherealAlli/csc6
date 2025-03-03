from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# frontend, new page, python scripts, connect to models

def test(request):
    return HttpResponse("Hello world!")
