from django.shortcuts import render

def verb(request):
    return render(request, "verb/verb.html", {})