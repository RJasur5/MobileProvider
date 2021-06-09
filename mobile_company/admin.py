from django.contrib import admin

from .models import *
admin.site.register(Providers)
admin.site.register(Dealers)
admin.site.register(Category)
admin.site.register(NumberCodes)
admin.site.register(PhoneNumbers)
admin.site.register(Tarif)
admin.site.register(Customer)
admin.site.register(Order)
