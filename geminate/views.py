from django.shortcuts import render

def geminate(request):
    return render(request, "geminate/geminate.html", {})