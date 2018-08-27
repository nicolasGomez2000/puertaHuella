from django.shortcuts import render
from django.http import HttpResponse
# Create your vie.ws here.
def hola(request):
    return HttpResponse("hola Mundo")
