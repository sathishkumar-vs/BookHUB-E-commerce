from django.urls import path
from .views import *

urlpatterns = [
    path('',login),
    path('logout/',logoutpage,name="logout"),
    path('signup/',signuppage),
]
