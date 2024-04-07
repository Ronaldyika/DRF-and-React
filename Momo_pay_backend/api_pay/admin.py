from django.contrib import admin
from .models import MoMoUser,PaymentTransaction

admin.site.register(MoMoUser)
admin.site.register(PaymentTransaction)