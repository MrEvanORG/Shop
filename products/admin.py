from django.contrib import admin
from .models import products , ordertickets ,buytickets

# Register your models here.

@admin.register(products)
class productsAdmin(admin.ModelAdmin):
    list_display = ("pistachio_name",
                    "pistachio_photo",
                    "pistachio_status",
                    "pistachio_per_ounce",
                    "pistachio_quality",
                    "pistachio_price",
                    "pistachio_gain_status",
                    "pistachio_gain",)
        
@admin.register(ordertickets)
class orderticketsAdmin(admin.ModelAdmin):
    list_display = ("ticket_id",
                    "buyer_namelastname",
                    "buyer_phone",
                    "request_title",
                    "request_discription",
                    "ticket_time",
                    "ip_address")
    readonly_fields = ("ticket_id","ticket_time")

@admin.register(buytickets)
class buyticketsAdmin(admin.ModelAdmin):
    list_display = ("ticket_id",
                    "buyer_namelastname",
                    "buyer_phone",
                    "pistachio",
                    "gain_product",
                    "order_discription",
                    "calculated_price",
                    "ticket_time",
                    "ip_address")
    readonly_fields = ("ticket_id","ticket_time")




# EehsaNn8404