from django.db import models


class MedicalIssue(models.Model):
    name = models.CharField(max_length=100)
    vaccineEligibility = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Industry model
class Industry(models.Model):
    name = models.CharField(max_length=100)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.name



# Patient model
class Patient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=6)
    emiratesID = models.CharField(max_length=15)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, blank=True, null=True)
    locationLat = models.FloatField(default=0)
    locationLng = models.FloatField(default=0)
    determination = models.BooleanField(default=False)
    dosesTaken = models.IntegerField(default=0)
    patientMedicalIssues = models.ManyToManyField(MedicalIssue, blank=True)

    def __str__(self):
        return self.email


# Admin model
class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email



