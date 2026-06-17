from django.contrib import admin
from .models import (
    QuoteRequest,
    Testimonial,
    SuccessStory,
    CompanyProfile,
    ShipmentProof,
    ProductGallery,
    FAQ,
)
# Register your models here.
admin.site.register(QuoteRequest)
admin.site.register(Testimonial)
admin.site.register(SuccessStory)
admin.site.register(CompanyProfile)
admin.site.register(ShipmentProof)
admin.site.register(ProductGallery)
admin.site.register(FAQ)