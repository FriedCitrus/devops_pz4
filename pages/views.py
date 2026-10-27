from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html")

def extra(request):
    return render(request, "pages/extra.html")

def phantasm(request):
    return render(request, "pages/phantasm.html")