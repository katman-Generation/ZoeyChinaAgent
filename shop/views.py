from django.shortcuts import render

from .forms import QuoteRequestForm


def home(request):

    form = QuoteRequestForm()

    return render(
        request,
        'shop/home.html',
        {
            'form': form
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