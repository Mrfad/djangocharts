from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_population = models.IntegerField()

    def __str__(self):
        return self.country_name

