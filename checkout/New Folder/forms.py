from django import forms

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2017, 2036)]

    
    credit_card_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Credit card number'}),
    max_length=16, label='Credit card number', required=True)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    cvv = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'cvv'}),
    max_length=3, label='Security code (CVV)', required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)