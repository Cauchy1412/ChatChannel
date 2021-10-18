# -*- coding: utf-8 -*-
from django.urls import path
from .views import api_register, api_login, history_msg, update_password, delete_msg

urlpatterns = [
    path('login/', api_login, name='api_login'),
    path('register/', api_register, name='api_register'),
    path('history_msg/', history_msg, name='history_msg'),
    path('update_password/', update_password, name='update_password'),
    path('delete_msg/', delete_msg, name='delete_msg'),
]
