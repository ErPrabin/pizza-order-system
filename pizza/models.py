from django.db import models
from django.utils import timezone

from accounts.models import CustomUser


# Create your models here.
class Pizza(models.Model):
    name=models.CharField(default=None, blank=False, null=False,max_length=200)
    price=models.IntegerField(default=None, blank=False, null=False)
    description=models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/pizza',null=True)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)
    updated_at= models.DateField(default=timezone.now)


    def __str__(self):
        return self.name

