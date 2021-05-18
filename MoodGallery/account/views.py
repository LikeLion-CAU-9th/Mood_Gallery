from django.shortcuts import render

# Create your views here.



def signinup(request):
    return render(request, 'signinup.html')