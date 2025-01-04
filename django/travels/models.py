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

    def __str__(self):
        return "User %s has visited country %s" % (self.user, self.country)
