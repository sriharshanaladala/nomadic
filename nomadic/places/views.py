from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def places(request):
    return HttpResponse("here are our best place to visit")

def place(request, pk):
    return HttpResponse("single place"+ '' + str(pk))