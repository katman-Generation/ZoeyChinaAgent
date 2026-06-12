from django import forms
from .models import QuoteRequest


class QuoteRequestForm(forms.ModelForm):

    class Meta:
        model = QuoteRequest

        fields = [
            'name',
            'email',
            'whatsapp',
            'country',
            'product_name',
            'quantity',
            'notes',
            'image',
        ]