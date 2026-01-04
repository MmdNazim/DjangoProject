from django.urls import path
from . import views
#url route here:
urlpatterns = [
    path('', views.home),
    path('product/', views.product),
    path('cart/', views.cart),
    path('checkout/', views.checkout),

]
