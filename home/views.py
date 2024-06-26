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

def demonstrativ_relativ_view(request):
    return render(request, 'demonstrativ_relativ/demonstrativ_relativ.html', {})

def sufix_posesiv_pl_view(request):
    return render(request, 'sufix_posesiv_pl/sufix_posesiv_pl.html', {})

def qal_infinitiv_view(request):
    return render(request, 'qal_infinitiv/qal_infinitiv.html', {})

def qal_activ_view(request):
    return render(request, 'qal_activ/qal_activ.html', {})

def sufix_pronominal_view(request):
    return render(request, 'sufix_pronominal/sufix_pronominal.html', {})

def este_si_are_view(request):
    return render(request, 'este_si_are/este_si_are.html', {})

def qal_volitiv_view(request):
    return render(request, 'qal_volitiv/qal_volitiv.html', {})


def qal_verbe_slabe_view(request):
    return render(request, 'qal_verbe_slabe/qal_verbe_slabe.html', {})

def relativ_waw_view(request):
    return render(request, 'relativ_waw/relativ_waw.html', {})

def temporal_interogativ_view(request):
    return render(request, 'temporal_interogativ/temporal_interogativ.html', {})

def piel_radacini_tari_view(request):
    return render(request, 'piel_radacini_tari/piel_radacini_tari.html', {})

def piel_radacini_slabe_view(request):
    return render(request, 'piel_radacini_slabe/piel_radacini_slabe.html', {})

def surpriza_view(request):
    return render(request, 'surpriza/surpriza.html', {})

def numeralul_view(request):
    return render(request, 'numeralul/numeralul.html', {})

def hiphil_radacini_tari_view(request):
    return render(request, 'hiphil_radacini_tari/hiphil_radacini_tari.html', {})

def hiphil_gutural_nun_view(request):
    return render(request, 'hiphil_gutural_nun/hiphil_gutural_nun.html', {})

def hiphil_yod_view(request):
    return render(request, 'hiphil_yod/hiphil_yod.html', {})

def hiphil_he_gaunoase_view(request):
    return render(request, 'hiphil_he_gaunoase/hiphil_he_gaunoase.html', {})

def pronume_mai_mult_view(request):
    return render(request, 'pronume_mai_mult/pronume_mai_mult.html', {})

def niphal_radacini_tari_view(request):
    return render(request, 'niphal_radacini_tari/niphal_radacini_tari.html', {})

def niphal_radacini_slabe_view(request):
    return render(request, 'niphal_radacini_slabe/niphal_radacini_slabe.html', {})

def verbe_pasive_view(request):
    return render(request, 'verbe_pasive/verbe_pasive.html', {})

def hithpael_view(request):
    return render(request, 'hithpael/hithpael.html', {})

def geminate_view(request):
    return render(request, 'geminate/geminate.html', {})