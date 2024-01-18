from django.shortcuts import render, redirect
from store.middlewares.auth import auth_middleware
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order
from django.utils.decorators import method_decorator

from django.views import View

class OrderView(View):
    
    @method_decorator(auth_middleware)
    def get(self,request): 
        customer = request.session.get('customer_id')
        orders1= Order.get_order_by_customer(customer) 
        print(orders1)
        return render(request , 'orders.html'  , {'order' : orders1})



    


