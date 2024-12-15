

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.Logout, name='logout'),
    path('newuser/', views.newuser, name='newuser'),
    path('users/', views.users, name='users'),
    path('deleteuser/<str:pk>/', views.deleteuser, name='deleteuser'),
    path('profile/', views.profile, name='profile'),
]


