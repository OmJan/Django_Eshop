from django.shortcuts import render, redirect
from store.models.product import Product
from store.models.category import Categories
from django.views import View


class home(View):
    def post(self, request):
        product = request.POST.get("product")
        cart = request.session.get("cart")
        remove = request.POST.get("remove")
        print(product, cart, remove)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session["cart"] = cart
        print(product, cart)

        return redirect("home")

    def get(self, request):
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        product = None
        category = Categories.get_all_category()
        categotyID = request.GET.get("category")
        if categotyID:
            product = Product.get_all_product_by_category_id(categotyID)
        else:
            product = Product.get_all_product()
        data = {}
        data["products"] = product
        data["category"] = category
        data["cart"] = request.session.get("cart")
        return render(request, "home.html", data)
