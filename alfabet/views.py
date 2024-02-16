from django.shortcuts import render
from django.http import HttpResponse

def alfabet(request):
    return render(request, "alfabet/alfabet.html", {})
