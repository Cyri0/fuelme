from django.db import models

# Create your models here.

class GasStation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Refuel(models.Model):
    gasstation = models.ForeignKey(GasStation, null=True, on_delete = models.SET_NULL)
    date = models.DateTimeField()

    petrol_types = [
        ('petrol95','petrol95'),
        ('petrol100','petrol100'),
        ('gas','gas'),
        ('diesel','diesel'),
    ]

    petrol_type = models.CharField(max_length=255, choices=petrol_types)
    amount = models.FloatField(default=0)
    distance = models.IntegerField()
    money = models.IntegerField()

    def __str__(self):
        return f"{self.gasstation} benzinkút - {self.date}"