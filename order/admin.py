from order.models import Order
from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
    list_display=('order_number','user','pizza','quantity','address','total_price')
    search_fields=['order_number','address','quantity','total_price']
    

# Register your models here.
admin.site.register(Order,OrderAdmin)
