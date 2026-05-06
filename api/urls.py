from django.urls import path
from .views import create_user, get_user, get_users, user_detail


urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/all', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail')
]