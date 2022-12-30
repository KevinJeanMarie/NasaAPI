from django.db import models

# Create your models here.


class Nasa(models.Model):

    title = models.CharField(max_length=255)
    due_data = models.DateField()
    description = models.CharField(max_length=255)
    kilometers = models.FloatField()
    meters = models.FloatField()
    miles = models.FloatField()
    feet = models.FloatField()
