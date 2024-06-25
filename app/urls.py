from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('banners/', views.banners, name='banners'),
    path('umbrella/', views.umbrella, name='umbrella'),

    path('checkout/<int:id_suscripcion>/', views.CheckOut, name='checkout'),
    path('payment-success/<int:id_suscripcion>/', views.PaymentSuccessful, name='payment-success'),
    path('payment-failed/<int:id_suscripcion>/', views.PaymentFailed, name='payment-failed'),
]