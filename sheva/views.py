from django.shortcuts import render
from django.http import HttpResponse

def sheva(request):
    return render(request, "sheva/sheva.html", {})