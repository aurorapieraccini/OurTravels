from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model): 
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class VisitedCountry(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class City(models.Model): 
    name = models.CharField(max_length=168)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class VisitedCities(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)        


    def __str__(self):
        return "User %s has visited country %s and city %s " % (self.user, self.country, self.city)
