from django.shortcuts import render

def numeralul(request):
    return render(request, "numeralul/numeralul.html", {})