from django.contrib import admin
from . models import Category,Product, customer, order


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(customer)
admin.site.register(order)