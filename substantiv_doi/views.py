from django.shortcuts import render

def substantiv_doi(request):
    return render(request, "substantiv_doi/substantiv_doi.html", {})