
# Register your models here.
from django.contrib import admin
from .models import Order
# Register your models here.
#admin
#1234

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    pass

