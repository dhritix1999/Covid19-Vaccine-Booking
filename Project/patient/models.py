from django.db import models



# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=6)
    emiratesID = models.IntegerField()
    industry = models.CharField(max_length=100)
    locationLat = models.FloatField()
    locationLng = models.FloatField()
    determination = models.BooleanField(default=False)
    dosesTaken = models.IntegerField(default=0)

    def __str__(self):
        return self.email
