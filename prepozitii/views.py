from django.shortcuts import render

def prepozitii(request):
    return render(request, "prepozitii/prepozitii.html", {})