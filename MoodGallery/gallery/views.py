from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def myboard(request):
    return render(request, 'myboard.html')

def index(request):
    return render(request, 'index.html')