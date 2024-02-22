from django.shortcuts import render

def pronume(request):
    return render(request, "pronume/pronume.html", {})