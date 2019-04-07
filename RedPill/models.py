from django.db import models

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
    is_relevant = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return "Location('{}', '{}', '{}')".format(self.title, self.price, self.date)


#loc = Location(title="test", price=850, date="date", description="test", charges_included=True, real_estate_type=0,
#               rooms=3, furnished=True, square=45.5, ges=0, energy_rate=0)
#loc.save()