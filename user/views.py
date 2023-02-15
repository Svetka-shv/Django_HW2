from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



def register(response):
    form = UserCreationForm()
    return render(response, "register.html", {"form":form})

def login(response):
    form = UserCreationForm()
    return render(response, "login.html", {"form":form})
