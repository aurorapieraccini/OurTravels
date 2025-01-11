from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

# def country(request, country_id):
#     try:
#         country = Country.objects.get(pk=country_id)
#     except Country.DoesNotExist:
#         raise Http404("Country does not exist")
#     return render(request, "travels/country.html", {"country": country})

def countries(request):
    return render(request, 'travels/countries.html')
     #countries = Country.objects.all()
    
#     return render(request, "travels/countries.html", {"countries": countries})
def ourtravels(request):
    return render(request, 'travels/ourtravels.html')

def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to Django admin
            return redirect('/admin/')
        else:
            messages.error(request, "Invalid username or password")
    return redirect('/')  # Redirect to the homepage or wherever you want

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Registration successful")
    return redirect('/')  # Redirect to the homepage or wherever you want