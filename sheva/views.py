from django.shortcuts import render

def sheva(request):
    return render(request, "sheva/sheva.html", {})