from order.models import Order
from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
    list_display=('user','pizza','quantity','address','phone_number','total_price','created_at')
    search_fields=['address','quantity','phone_number','total_price']
    

# Register your models here.
admin.site.register(Order,OrderAdmin)
