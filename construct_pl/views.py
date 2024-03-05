from django.shortcuts import render

def construct_pl(request):
    return render(request, "construct_pl/construct_pl.html", {})