from django.shortcuts import render, redirect
from store.models.customer import Customer
from store.models.product import Product
from store.models.orders import Order

from django.views import View


class CheckOut(View):
    def post(self, request):
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer_id")
        cart = request.session.get("cart")
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            order = Order(
                customer=Customer(id=customer),
                product=product,
                price=product.price,
                phone=phone,
                address=address,
                quantity=cart.get(str(product.id)),
            )
            order.save()
        request.session["cart"] = {}
        return redirect("payment")


def payment(request):
    return render(request, "payment.html")
