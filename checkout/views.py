from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from checkout.forms import MakePaymentForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template.context_processors import csrf
from django.conf import settings
from babysitters.models import Babysitter
import stripe

# stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url="/accounts/login")
def buy_now(request, id):
    if request.method == 'POST':
        form = MakePaymentForm(request.POST)
        if form.is_valid():
            try:
                babysitter = get_object_or_404(Babysitter, pk=id)
                customer = stripe.Charge.create(
                    amount= int(babysitter.price * 100),
                    currency="EUR",
                    description=babysitter.firstName,
                    card=form.cleaned_data['stripe_id'],
                )
            except (stripe.error.CardError):
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            messages.error(request, "We were unable to take a payment with that card!")

    else:
        form = MakePaymentForm()
        babysitter = get_object_or_404(Babysitter, pk=id)

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'babysitter': babysitter}
    args.update(csrf(request))

    return render(request, 'checkout.html', args)