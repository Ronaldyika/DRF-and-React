from django.contrib import admin
from .models import Product,ProductImage,CartItem,Communication

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(CartItem)
admin.site.register(Communication)