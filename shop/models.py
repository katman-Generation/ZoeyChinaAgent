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
    
class Testimonial(models.Model):

    customer_name = models.CharField(max_length=100)

    country = models.CharField(max_length=100)

    review = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.customer_name
    
class SuccessStory(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
class CompanyProfile(models.Model):

    company_name = models.CharField(max_length=200)

    owner_name = models.CharField(max_length=200)

    business_address = models.TextField()

    whatsapp = models.CharField(max_length=50)

    email = models.EmailField()

    about = models.TextField()

    photo = models.ImageField(
        upload_to='company/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.company_name
    
class ProductGallery(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='gallery/'
    )

    def __str__(self):
        return self.title
    
class ShipmentProof(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='shipments/'
    )

    def __str__(self):
        return self.title
    
class FAQ(models.Model):

    question = models.CharField(max_length=300)

    answer = models.TextField()

    def __str__(self):
        return self.question