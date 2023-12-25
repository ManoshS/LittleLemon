from django.db import models

# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=255)
    No_of_guests=models.IntegerField()
    bookingDate=models.DateField()

class Menu(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    inventry =models.IntegerField()
    
    def get_item(self):
        return f'{self.title}:{str(self.price)}'
