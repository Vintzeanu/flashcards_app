from django.shortcuts import render

def substantiv(request):
    return render(request, "substantiv/substantiv.html", {})