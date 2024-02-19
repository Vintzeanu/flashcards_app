from django.shortcuts import render

def alfabet(request):
    return render(request, "alfabet/alfabet.html", {})
