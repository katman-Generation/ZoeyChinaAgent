from django.shortcuts import render, get_object_or_404

from .models import (
    Testimonial,
    SuccessStory,
    ShipmentProof,
    CompanyProfile,
    ProductCategory,
    Product,
    FAQ,
)

from .forms import QuoteRequestForm


def home(request):
    
    selected_product = None
    
    product_id = request.GET.get('product')
    if product_id:
        try:
            selected_product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            selected_product = None
            
    form = QuoteRequestForm(
        initial={'product_name': selected_product.title }
        if selected_product else None
    )

    testimonials = Testimonial.objects.all()
    success_stories = SuccessStory.objects.all()
    company_profile = CompanyProfile.objects.first()

    # Products grouped through their categories
    product_categories = ProductCategory.objects.all()

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
            'product_categories': product_categories,
            'shipment_proofs': shipment_proofs,
            'faq': faq,
            'selected_product': selected_product,
        }
    )

def category_products(request, category_id):

    category = get_object_or_404(
        ProductCategory,
        id=category_id
    )

    categories = ProductCategory.objects.all()

    products = Product.objects.filter(
        category=category
    ).prefetch_related(
        'images'
    )

    return render(
        request,
        'shop/partials/category_products.html',
        {
            'category': category,
            'categories': categories,
            'products': products,
        }
    )
    
def product_detail(request, product_id):

    product = get_object_or_404(
        Product.objects.prefetch_related('images'),
        id=product_id
    )

    categories = ProductCategory.objects.all()

    return render(
        request,
        'shop/partials/product_detail.html',
        {
            'product': product,
            'categories': categories,
        }
    )


def submit_quote(request):

    if request.method == "POST":

        form = QuoteRequestForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            quote = form.save(commit=False)

            product_id = request.POST.get('product')

            if product_id:

                try:

                    quote.product = Product.objects.get(
                        id=product_id
                    )

                except Product.DoesNotExist:

                    quote.product = None

            quote.save()

            return render(
                request,
                'shop/partials/success_message.html'
            )

    else:

        form = QuoteRequestForm()

    return render(
        request,
        'shop/partials/quote_form.html',
        {
            'form': form
        }
    )