from django.urls import path

from food.views import *

urlpatterns = [
    path('login', login),
    path('register', register),
    path('get_user', get_user),
    path('update_user', update_user),

]
