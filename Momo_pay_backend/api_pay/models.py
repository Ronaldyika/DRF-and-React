# models.py
from django.db import models

class MoMoUser(models.Model):
    userId = models.CharField(max_length=100, unique=True)
    apiKey = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.userId



class PaymentTransaction(models.Model):
    userId = models.CharField(max_length=100)
    apiKey = models.CharField(max_length=100)
    # Other fields if needed

    def __str__(self):
        return self.userId  # Or any other field you want to represent the object

    class Meta:
        verbose_name = "Payment User"
        verbose_name_plural = "Payment Users"



class Payments(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f'PaymentTransaction - Ref ID: {self.payment_ref_id}'
