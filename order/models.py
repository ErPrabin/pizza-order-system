from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from pizza.models import Pizza

from accounts.models import CustomUser


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=None, blank=False, null=False)
    total_price=models.IntegerField(default=None, blank=False, null=False)
    phone_number=models.CharField(max_length=15,default=None, blank=False, null=False)
    address=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateField(default=timezone.now)


    # def __str__(self):
    #     return self.name

