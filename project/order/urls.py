from django.urls import path
from .views import to_cart, cart, checkout, orders, cancel_order

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/<int:ad_id>/<str:action>/', to_cart, name='to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),
    path('orders/<int:order_id>/cancel/', cancel_order, name='cancel_order'),
]
