from django.shortcuts import render

def hithpael(request):
    return render(request, "hithpael/hithpael.html", {})