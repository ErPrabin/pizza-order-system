from pizza.models import Pizza
from django.contrib import admin

class PizzaAdmin(admin.ModelAdmin):
    list_display=('name','price','description','image','created_at')
    search_fields=['name','price','description']
    
    readonly_fields=('image',)

    def image(self, obj):
        return obj.image

    image.short_description = 'Blog Image'
    image.allow_tags = True
# Register your models here.
admin.site.register(Pizza,PizzaAdmin)
