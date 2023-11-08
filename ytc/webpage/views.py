from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):

    return render(request, "home.html")

def pets(request):
    return render(request, "pets.html")


def donate(request):
    return render(request, "donate.html")