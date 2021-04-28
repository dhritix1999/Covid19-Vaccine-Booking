from django.db import models

# Create your models here.

class BookingSlot(models.Model):
    centerID = models.IntegerField()
    timeSlot = models.DateTimeField()
    bookingCount = models.IntegerField(default=0)

    def __str__(self):
        return str(self.timeSlot)

class Booking(models.Model):
    bookingSlotID = models.IntegerField()
    patientID = models.IntegerField()

    def __str__(self):
        return str(self.bookingSlotID) + ' - ' + str(self.patientID)
