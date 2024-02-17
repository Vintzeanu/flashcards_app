from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home/welcome.html", {})

def alfabet_view(request):
    return render(request, 'alfabet/alfabet.html', {})

def vowels_view(request):
    return render(request, 'vowels/vowels.html', {})