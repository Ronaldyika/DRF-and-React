from django.contrib import admin
from .models import MoMoUser,PaymentTransaction,Payments

admin.site.register(MoMoUser)
admin.site.register(PaymentTransaction)
admin.site.register(Payments)