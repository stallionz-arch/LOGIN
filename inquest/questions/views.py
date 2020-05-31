from django.shortcuts import render

# Create your views here.


def questions_home(request):
    return render(request, 'questions/home.html')


def details(request):
    return render(request, 'questions/home.html')
