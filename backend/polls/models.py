from django.db import models


# Create your models here.
class Poll(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Vehicle(models.Model):
    pass


class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


class Wheel(models.Model):
    pass