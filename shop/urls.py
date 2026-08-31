from django.urls import path
from .views import home, product_detail, submit_quote, category_products

urlpatterns = [
    path('', home, name='home'),
    path(
        'Products/category/<int:category_id>/',
        category_products,
        name='category_products'
    ),
    path(
        'Products/<int:product_id>/',
        product_detail,
        name='product_detail'
    ),
    path(
        'submit-quote/',
        submit_quote,
        name='submit_quote'
    ),
]