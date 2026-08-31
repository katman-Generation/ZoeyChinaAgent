from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import (
    QuoteRequest,
    Testimonial,
    SuccessStory,
    CompanyProfile,
    ShipmentProof,
    ProductCategory,
    Product,
    ProductImage,
    FAQ,
)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)
    inlines = [ProductImageInline]
    
# Register your models here.
@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'whatsapp',
        'product_link',
        'quantity',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'product',
        'created_at',
    )

    search_fields = (
        'name',
        'whatsapp',
        'email',
        'product_name',
    )

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'created_at',
    )

    def product_link(self, obj):

        if obj.product:

            url = reverse(
                'admin:shop_product_change',
                args=[obj.product.id]
            )

            return format_html(
                '<a href="{}">{}</a>',
                url,
                obj.product.title
            )

        return obj.product_name or '-'

    product_link.short_description = 'Product'
    
    
admin.site.register(Testimonial)
admin.site.register(SuccessStory)
admin.site.register(CompanyProfile)
admin.site.register(ShipmentProof)
admin.site.register(ProductCategory)
admin.site.register(FAQ)