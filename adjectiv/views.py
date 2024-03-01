from django.shortcuts import render

def adjectiv(request):
    return render(request, "adjectiv/adjectiv.html", {})
