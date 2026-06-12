from django.db import models

# Create your models here.
from django.db import models


class QuoteRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('quoted', 'Quoted'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    whatsapp = models.CharField(max_length=30)
    country = models.CharField(max_length=100)

    product_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()

    notes = models.TextField(blank=True)

    image = models.ImageField(
        upload_to='quote_requests/',
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product_name}"