from django.db import models
from datetime import datetime

class Location(models.Model):
    """ Contains all data available concerning a location """

    url = models.CharField(max_length=250, default="")
    city = models.CharField(max_length=200, default="")
    postal_code = models.CharField(max_length=5, default="00000")
    title = models.CharField(max_length=200, default="")
    price = models.IntegerField(default=0)
    date = models.DateField(default="1999-01-01")
    description = models.TextField(default="")
    charges_included = models.BooleanField(default=False)
    owner_is_pro = models.BooleanField(default=False)
    real_estate_type = models.IntegerField(default=0)
    rooms = models.IntegerField(default=0)
    furnished = models.BooleanField(default=False)
    square = models.FloatField(default=0)
    ges = models.IntegerField(default=0)
    energy_rate = models.IntegerField(default=0)
    images = models.CharField(max_length=1000, default="")
    has_been_seen = models.BooleanField(default=False)
    is_relevant = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return "Location('{}', '{}', '{}')".format(self.title, self.price, self.date)

class SearchLocation(models.Model):
    search_date = models.DateTimeField(default=datetime.now, blank=True)
    
