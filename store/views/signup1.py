from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class signup1(View):
    def get(self, request):
        return render(request, "signup1.html")

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Validation
        value = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
        }
        error_message = None
        # Data is valid, create the Customer object
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
        )
        error_message = self.validateCustomer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()  # Save the customer to the database

            # Redirect to the home page after successful registration
            return redirect("home")
        else:
            value = {
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
                "email": email,
            }

        data = {"error": error_message, "values": value}
        return render(request, "signup1.html", data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First name is required."
        elif len(customer.first_name) < 4:
            error_message = "First name must be 4 characters or more."
        elif not customer.phone:
            error_message = "Phone number is required."
        elif len(customer.phone) < 10:
            error_message = "Phone number must be 10 characters or more."
        elif len(customer.password) < 6:
            error_message = "Password must be 6 characters or more."
        elif len(customer.email) < 5:
            error_message = "Email must be 5 characters or more."
        elif customer.isExists():
            error_message = "Email already  Exists"
        return error_message
