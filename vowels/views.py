from django.shortcuts import render

def vowels(request):
    return render(request, "vowels/vowels.html", {})