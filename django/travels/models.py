from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.

class City(models.Model): 
    name = models.CharField(max_length=168)
    country = CountryField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null = True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null = True)
    #postal_code = models.CharField(max_length=20, null = True)
    #state = models.CharField(max_length=100, null = True)
    #province = models.CharField(max_length=100, null = True)
    population = models.PositiveIntegerField(null = True)
    elevation = models.IntegerField(null = True)
    #timezone = models.DateTimeField()
    modification_date = models.DateField(null = True)
    geonameid = models.IntegerField(null = True)

    def __str__(self):
        return self.name

class VisitedCities(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)        

    def __str__(self):
        return "User %s has visited country %s and city %s " % (self.user, self.country, self.city)
