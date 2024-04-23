from django.db import models

# Create your models here.
class Booking(models.Model):
  name = models.CharField(max_length=255)
  no_of_guests = models.SmallIntegerField(default=1)
  booking_date = models.DateField(db_index=True)

class Menu(models.Model):
  title = models.CharField(max_length=255, db_index=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  inventory = models.SmallIntegerField(default=0)