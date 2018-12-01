from django import forms
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .models import KidProfile
from .models import UserProfile


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

# class FullUserDetailsForm(forms.ModelForm):
#      class Meta:
#          model=UserProfile
#          fields = ['user', 'first_name', 'last_name', 'address1', 'address2','postcode','phone', 'dob', 'gender']

class FullUserDetailsForm(forms.Form):
    first_name = forms.CharField(max_length=None, required=False)
    last_name = forms.CharField(max_length=None, required=False)
    image = forms.ImageField(max_length=None, required=False)
    address1 = forms.CharField(max_length=255, required=False)
    address2 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=255, required=False)
    county = forms.CharField(max_length=255, required=False)
    biography = forms.CharField(max_length=255, required=False)
    postcode = forms.CharField(max_length=7, required=False)
    email = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=10, required=False)
    dob = forms.CharField(max_length=10, required=False)
    gender = forms.CharField(max_length=1, required=False)
    facebook = forms.CharField(max_length=50, required=False)
    twitter = forms.CharField(max_length=50, required=False)
    instagram = forms.CharField(max_length=50, required=False)

    # finish this


class KidDetailsForm(forms.Form):
    name = forms.CharField(max_length=None, required=False)
    dob = forms.CharField(max_length=10, required=False)
    gender = forms.CharField(max_length=1, required=False)
    needs = forms.CharField(max_length=3, required=False)


# class KidProfileForm(forms.ModelForm):
#     class Meta:
#         model=KidProfile
#         fields = ['name', 'dob', 'gender', 'needs']
        # Finish this



class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2
        
