from django.contrib import admin
from django.urls import path


# localhost/account/~

import account.views

urlpatterns = [
    path('', account.views.login, name='login'),
    path('new-account', account.views.new_account, name='new_account'),

]
