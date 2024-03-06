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

def substantiv_doi_view(request):
    return render(request, 'substantiv_doi/substantiv_doi.html', {})

def prepozitii_view(request):
    return render(request, 'prepozitii/prepozitii.html', {})

def adjectiv_view(request):
    return render(request, 'adjectiv/adjectiv.html', {})

def qal_imperfect_view(request):
    return render(request, 'qal_imperfect/qal_imperfect.html', {})

def construct_sg_view(request):
    return render(request, 'construct_sg/construct_sg.html', {})

def construct_pl_view(request):
    return render(request, 'construct_pl/construct_pl.html', {})

def qal_radacini_slabe_view(request):
    return render(request, 'qal_radacini_slabe/qal_radacini_slabe.html', {})

def sufix_posesiv_subst_view(request):
    return render(request, 'sufix_posesiv_subst/sufix_posesiv_subst.html', {})