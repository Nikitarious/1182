from django.contrib import admin
from django.urls import path

app_name = 'admins'

from .views import index,admin_users_delete,UserUpdateView ,UserCreateView,UserListView
    # admin_users , admin_users_create,admin_users_update

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('user-update/<int:pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('user-delete/<int:id>', admin_users_delete, name='admin_users_delete'),
]
