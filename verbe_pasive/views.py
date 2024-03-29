from django.shortcuts import render

def verbe_pasive(request):
    return render(request, "verbe_pasive/verbe_pasive.html", {})