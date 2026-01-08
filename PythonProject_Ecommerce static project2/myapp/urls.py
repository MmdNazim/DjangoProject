from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('product/', views.product),
    path('cart/', views.cart),
    path('checkout/', views.checkout),
    path('typesofresponse/', views.TypesOfResponse),
    path('typesofrequest/', views.TypesOfRequest),

]
