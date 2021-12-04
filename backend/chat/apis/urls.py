# -*- coding: utf-8 -*-
from django.urls import path
from .views import api_register, api_login, history_msg, join_room, update_password, delete_msg, add_chat_room, join_room, add_dynamic, add_comment, get_dynamics

urlpatterns = [
    path('login/', api_login, name='api_login'),
    path('register/', api_register, name='api_register'),
    path('history_msg/', history_msg, name='history_msg'),
    path('update_password/', update_password, name='update_password'),
    path('delete_msg/', delete_msg, name='delete_msg'),
    path('add_chat_room/', add_chat_room, name='add_chat_room'),
    path('room_add_person/', join_room, name = 'room_add_person'),
    path('add_dynamic/', add_dynamic, name='add_dynamic'),
    path('add_comment/', add_comment, name='add_comment'),
    path('get_dynamics/', get_dynamics, name='get_dynamics'),
]
