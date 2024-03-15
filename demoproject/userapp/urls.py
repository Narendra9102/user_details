from django.urls import path
from userapp.views import *

urlpatterns = [
    path('',index,name='home'),
    path('add_user/', add_user, name='add_user'),
    path('user_details/', user_details, name='user_details'),
]