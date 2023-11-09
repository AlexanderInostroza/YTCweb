from django.shortcuts import render
import os

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, "home.html")

def pets(request):
    i = 0
    dir = "ytc/webpage/static/content/adopcion"
    files = os.listdir(dir)
    pets = []
    for file in files:
        name, extension = file.split(".")
        if extension != "txt":
            pets.append({
                "name": name,
                "img": file,
            })
    context = {"pets": pets}
    return render(request, "pets.html", context)


def donate(request):
    return render(request, "donate.html")