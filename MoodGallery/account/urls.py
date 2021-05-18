from django.contrib import admin
from django.urls import path


# localhost/account/~

import account.views

urlpatterns = [
    path('', account.views.signinup, name='signinup'),
    

]
