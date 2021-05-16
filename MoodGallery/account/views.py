from django.shortcuts import render

# Create your views here.

def new_account(request):
    return render(request, 'new_account.html')

def login(request):
    return render(request, 'login.html')