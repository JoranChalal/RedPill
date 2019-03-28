from django.db import models

class Location(models.Model):
    """ Contains all data available concerning a location """

    title = models.CharField(max_length=200)
    price = models.IntegerField()
    date = models.DateField()
    description = models.TextField()
    charges_included = models.BooleanField()
    real_estate_type = models.IntegerField()
    rooms = models.IntegerField()
    furnished = models.BooleanField()
    square = models.FloatField()
    ges = models.IntegerField()
    energy_rate = models.IntegerField()

    def __str__(self):
        return "Location('{}', '{}', '{}')".format(self.title, self.price, self.date)


#loc = Location(title="test", price=850, date="date", description="test", charges_included=True, real_estate_type=0,
#               rooms=3, furnished=True, square=45.5, ges=0, energy_rate=0)
#loc.save()