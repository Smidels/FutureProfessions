from django.urls import path
from .views import *

urlpatterns = [

    path('logout/', user_logout, name='logout'),
    path('sign-in/', user_login, name='user_login'),
    path('sign-up/', user_registration, name='user_registration'),
    path('edit_profile/<customuser_pk>', EditProfile.as_view(), name='edit_profile'),


]
