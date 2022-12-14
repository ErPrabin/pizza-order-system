from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import render
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from pizza.models import Pizza
from order.models import Order
from django.contrib import messages
import json

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})


def checkout(request, id):
    pizza = Pizza.objects.get(pk=id)
    try:
        return render(request, 'checkout.html', {'pizza': pizza})

    except Pizza.DoesNotExist:
        messages.error(request, 'Book Doesnot Exist.')
        return redirect('/')


def order(request):
    print(request.POST['quantity'])
    order = Order(user_id=request.user.id, pizza_id=request.POST['pizza_id'], quantity=request.POST[
                  'quantity'],phone_number=request.POST['phone_number'] ,address=request.POST['address'], total_price=request.POST['total_price'])
    order.save()
    messages.success(request, 'Order Placement Successful')
    return redirect('/success')

def success(request):
    return render(request, 'success.html')

