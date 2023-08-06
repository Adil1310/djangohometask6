from django.db import models

# Create your models here.

class IceCream(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    icecream = models.ForeignKey(IceCream, on_delete=models.CASCADE)

    def __str__(self):
        return self.name