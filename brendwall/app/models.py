from django.db import models
from rest_framework.exceptions import ParseError

class Product(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True) # blank for self-validation
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True) # blank for self-validation

    def __str__(self):
        return f"{self.title} - {self.price}"
