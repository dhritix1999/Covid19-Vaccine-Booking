from django.db import models

# Create your models here.
class VaccineCenter(models.Model):
    name = models.CharField(max_length=100)
    locationLat = models.FloatField(default=0)
    locationLng = models.FloatField(default=0)
    dosesStock = models.IntegerField(default=0)
    dosesPerHour = models.IntegerField(default=0)

    def __str__(self):
        return self.name