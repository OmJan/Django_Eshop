from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from store.models.product import Product
from store.models.category import Categories
from store.models.orders import Order
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View