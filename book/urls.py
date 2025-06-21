from django.urls import path
from .views import *

urlpatterns = [
    path('home/',homepage,name="homepage"),
    path('category/<str:category_name>/',books_by_category,name='books_by_category'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:cart_id>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:cart_id>/', decrease_quantity, name='decrease_quantity'),
    path('cart/', view_cart, name='cart'),
    path('place-order/', place_order, name='place_order'),
    path('my-orders/', my_orders, name='my_orders'),
    path('fake-payment/', fake_payment, name='fake_payment'),
    path('order-success/', order_success, name='order_success'),
]
