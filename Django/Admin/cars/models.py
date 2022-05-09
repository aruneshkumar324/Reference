from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime as dt


current_year = dt.now().year


class Car(models.Model):
    brand = models.CharField(max_length=50)
    year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(current_year)])

    def __str__(self):
        return f"{self.brand} - {self.year}"