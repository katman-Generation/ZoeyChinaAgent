from django.shortcuts import render
from .models import (
    Testimonial,
    SuccessStory,
    ShipmentProof,
    CompanyProfile,
    ProductGallery,
    FAQ
)
from .forms import QuoteRequestForm


def home(request):

    form = QuoteRequestForm()
    
    testimonials = Testimonial.objects.all()
    success_stories = SuccessStory.objects.all()
    company_profile = CompanyProfile.objects.first()
    product_gallery = ProductGallery.objects.all()
    shipment_proofs = ShipmentProof.objects.all()
    faq = FAQ.objects.all()
    
    return render(
        request,
        'shop/home.html',
        {
            'form': form,
            'testimonials': testimonials,
            'success_stories': success_stories,
            'company_profile': company_profile,
            'product_gallery': product_gallery,
            'shipment_proofs': shipment_proofs,
            'faq': faq
        }
    )


def submit_quote(request):

    if request.method == "POST":

        form = QuoteRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return render(
                request,
                'shop/partials/success_message.html'
            )

    return render(
        request,
        'shop/partials/quote_form.html',
        {
            'form': form
        }
    )