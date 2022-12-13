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
from django.contrib import messages
import json

# Create your views here.

@login_required(login_url='/login/')
def index(request):
    pizzas= Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})
