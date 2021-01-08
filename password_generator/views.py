from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, "generator/home.html")

def password(request):
    return render(request, "generator/password.html")

def postPassword(request):
    inp = request.GET
    string="abcdefghijklmnopqrstuvwxyz"
    characters = list(string)
    num = "0123456789"
    sep = "!@#$%^&*()_"
    # Processing
    thepassword = ""
    lenght = int(inp.get("length", "8"))

    if inp.get("upper"):
        characters.extend(list(string.upper()))
    if inp.get("num"):
        characters.extend(list(num))
    if inp.get("sep"):
        characters.extend(list(sep))
    for x in range(lenght):
        thepassword += random.choice(characters)

    return HttpResponse(thepassword)
