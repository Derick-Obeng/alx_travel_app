from django.db import models

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Human‑readable representation in Django admin and shell."""
        return self.name
