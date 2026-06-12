from django.urls import path
from .views import home, submit_quote

urlpatterns = [
    path('', home, name='home'),

    path(
        'submit-quote/',
        submit_quote,
        name='submit_quote'
    ),
]