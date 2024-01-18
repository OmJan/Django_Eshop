from django.urls import path
from store import views
from .views.login import Login, logout
from .views.signup1 import signup1
from .views.home import home 
from .views.cart import cart
from .views.checkout import CheckOut, payment
from .views.orders import OrderView
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('',home.as_view(),name="home"),
    path('login',Login.as_view(), name='login'),
    path('signup1',signup1.as_view(), name='signup1'),
    path('logout/', logout,name='logout' ),
    path('cart', auth_middleware(cart.as_view()),name='cart' ),
    path('check-out', CheckOut.as_view(),name='checkout' ),
    path('orders', auth_middleware(OrderView.as_view()),name='orders' ),
    path('payment', payment, name='payment'), 

] 