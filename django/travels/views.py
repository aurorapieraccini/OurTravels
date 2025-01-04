from django.shortcuts import render
from django.http import Http404
from .models import *
  
# Create your views here.

def country(request, country_id):
    try:
        country = Country.objects.get(pk=country_id)
    except Country.DoesNotExist:
        raise Http404("Country does not exist")
    return render(request, "travels/country.html", {"country": country})

def countries(request):
    countries = Country.objects.all()
    
    return render(request, "travels/countries.html", {"countries": countries})
