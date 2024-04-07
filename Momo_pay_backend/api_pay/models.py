# models.py

from django.db import models

class MoMoUser(models.Model):
    user_id = models.CharField(max_length=32)
    api_key = models.CharField(max_length=255)
  

class PaymentTransaction(models.Model):
    transaction_id = models.CharField(max_length=32)
    momo_token_id = models.CharField(max_length=255)
