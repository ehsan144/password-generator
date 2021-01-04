from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, "generator/home.html")


def password(request):
    # defult Data
    sting = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    sep = "!@#$%^&*()_"
    inp = request.GET

    # processing
    tpassword = ""
    characters = list(sting)
    lenght = int(inp.get("length", "8"))

    if inp.get("upper"):
        characters.extend(list(sting.upper()))
    if inp.get("num"):
        characters.extend(list(num))
    if inp.get("sep"):
        characters.extend(list(sep))
    for x in range(lenght):
        tpassword += random.choice(characters)
    return render(request, "generator/password.html", {"password": tpassword})
