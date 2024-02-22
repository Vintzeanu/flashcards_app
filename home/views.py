from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home/welcome.html", {})

def alfabet_view(request):
    return render(request, 'alfabet/alfabet.html', {})

def vowels_view(request):
    return render(request, 'vowels/vowels.html', {})

def sheva_view(request):
    return render(request, 'sheva/sheva.html', {})

def substantiv_view(request):
    return render(request, 'substantiv/substantiv.html', {})

def pronume_view(request):
    return render(request, 'pronume/pronume.html', {})