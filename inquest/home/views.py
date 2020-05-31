from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def web(request):
    return render(request, 'home/webd.html')


def index(request):
    return render(request, 'home/index.htm')

@login_required
def login_dashboard(request):
    return render(request, 'home/dashboard.html')