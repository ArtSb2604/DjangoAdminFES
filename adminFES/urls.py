from django.contrib import admin
from django.urls import path, include, re_path

from adminFES.views import Index, logout_admin, UserList

urlpatterns = [
    path('', Index.as_view(), name='index_admin'),
    path('users/', UserList.as_view(), name='users'),
    path('admin_logout/', logout_admin, name='logout_admin'),
]
