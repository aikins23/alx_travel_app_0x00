from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("WELCOME TO MY BOOKSTORE")

# Create your views here.
