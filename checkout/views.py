from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from checkout.forms import MakePaymentForm, OrderForm
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template.context_processors import csrf
from django.conf import settings
from django.utils import timezone
from babysitters.models import Babysitter
from .models import OrderLineItem
import stripe

# stripe.api_key = settings.STRIPE_SECRET


@login_required(login_url="/accounts/login")
def checkout(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            bookings = request.session.get('bookings', {})
            total = 0
            for id, quantity in bookings.items():
                babysitter = get_object_or_404(Babysitter, pk=id)
                total += quantity * babysitter.price
                order_line_item = OrderLineItem(
                    order = order, 
                    babysitter = babysitter, 
                    quantity = quantity
                    )
                order_line_item.save()
                
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})
    
    stripe.api_key = settings.STRIPE_SECRET

                
            