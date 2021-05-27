from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("HELLO !! WELCOME TO JAY WORLD!!")
# Create your views here.
