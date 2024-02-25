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

def verb_view(request):
    return render(request, 'verb/verb.html', {})

def qal_perfect_view(request):
    return render(request, 'qal_perfect/qal_perfect.html', {})

def propozitii_view(request):
    return render(request, 'propozitii/propozitii.html', {})