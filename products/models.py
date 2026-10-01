from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
