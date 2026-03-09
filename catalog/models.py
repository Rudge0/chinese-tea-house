from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


def max_current_year(value):
    current_year = datetime.now().year
    if value > current_year:
        raise ValidationError(f'Year cannot be greater than {current_year}')


class TeaCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)


class Province(models.Model):
    name = models.CharField(max_length=255)


class Supplier(AbstractUser):
    website = models.URLField(blank=True, null=True)


class Tea(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    harvest_year = models.IntegerField(validators=[
            MinValueValidator(0),
            max_current_year
        ])

    category = models.ForeignKey(
        TeaCategory,
        on_delete=models.CASCADE,
        related_name="teas"
    )

    region = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="teas"
    )

    supplier = models.ManyToManyField(Supplier, related_name="teas")
