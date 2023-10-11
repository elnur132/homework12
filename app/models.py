from django.db import models

# Create your models here.
class Truck(models.Model):
    brand = models.CharField(max_length=100)
    engine = models.IntegerField()
    color = models.CharField(max_length=100)
    type_of = models.CharField(max_length=100)

    def __str__(self):
        return self.brand