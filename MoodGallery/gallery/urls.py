from django.contrib import admin
from django.urls import path

# localhost/gallery/~

import gallery.views

urlpatterns = [
    path('', gallery.views.home, name='home'),
    path('myboard/', gallery.views.myboard, name='myboard'),

]
