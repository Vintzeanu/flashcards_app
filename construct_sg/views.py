from django.shortcuts import render

def construct_sg(request):
    return render(request, "construct_sg/construct_sg.html", {})