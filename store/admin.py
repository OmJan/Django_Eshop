from django.contrib import admin
from .models.product import Product
from .models.category import Categories
from .models.customer import Customer
from .models.orders import Order
from django.utils.safestring import mark_safe


class AdminProduct(admin.ModelAdmin):
    list_display = ["name","price","desciption",'display_image']
    
    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
    display_image.short_description = "Image"


class AdminCategory(admin.ModelAdmin):
    list_display = ["name"]


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Categories, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
