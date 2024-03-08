from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price= models.DecimalField(max_digit = 10,decimal_places = 2)

    def __str__(self):
        return self.name
class  ProductImage(models.Model):
    product = models.ForeignKey(Product,related_name = 'image',on_delete = models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return self.product.name + 'image'
    
class CartItem(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name = 'cart_items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name = 'product')
    quantity = models.PositiveIntegerField(default = 1)


    def __str__(self):
        return self.product.name
    
class Communication(models.Model):
    user = models.ForeignKey(Customer,related_name='communication', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.TextField()
    admin_reply = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return 