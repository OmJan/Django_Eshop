from django.shortcuts import render, redirect
from store.models.product import Product
from django.views import View

class cart(View):
    def get(self,request): 
        ids = list(request.session.get('cart').keys())
        product = Product.get_products_by_id(ids)
        return render(request, "cart.html",{"product":product})



    
 