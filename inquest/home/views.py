from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home/webd.html')


def web(request):
    return render(request, 'home/home.html')