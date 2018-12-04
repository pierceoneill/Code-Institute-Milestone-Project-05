from django import forms
from .models import Order

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2018, 2036)]

    
    credit_card_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Credit card number'}),
    max_length=16, label='Credit card number', required=True)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    cvv = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'cvv'}),
    max_length=3, label='Security code (CVV)', required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phone', 'postcode', 'city', 'address1', 'address2', 'county')