from django.shortcuts import render

def surpriza(request):
    return render(request, "surpriza/surpriza.html", {})