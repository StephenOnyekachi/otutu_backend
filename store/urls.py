

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('tocart/<str:pk>/', views.tocart, name='tocart'),
    path('cart/', views.cart, name='cart'),
    path('remove_cart/<str:pk>/', views.remove_cart, name='remove_cart'),
    path('newitem/', views.newitem, name='newitem'),
    path('viewitem/<str:pk>/', views.viewitem, name='viewitem'),
    path('deleteitem/<str:pk>/', views.deleteitem, name='deleteitem'),
    path('is_avaliable/<str:pk>/', views.is_avaliable, name='is_avaliable'),
    path('dashboad/', views.dashboad, name='dashboad'),
    path('pricelist/', views.pricelist, name='pricelist'),
    path('sells/', views.sells, name='sells'),
    path('credite/', views.credite, name='credite'),
    path('paid/<str:pk>/', views.paid, name='paid'),
    path('order/', views.order, name='order'),
    path('is_paid/<str:pk>/', views.is_paid, name='is_paid'),
    path('is_suplied/<str:pk>/', views.is_suplied, name='is_suplied'),
    path('search', views.search, name='search'),
    path('search2', views.search2, name='search2'),
]


