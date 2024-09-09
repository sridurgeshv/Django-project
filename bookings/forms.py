from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking, TravelOption

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TravelFilterForm(forms.Form):
    type = forms.ChoiceField(choices=[('', 'All')] + list(TravelOption.TRAVEL_TYPES), required=False)
    source = forms.CharField(max_length=100, required=False)
    destination = forms.CharField(max_length=100, required=False)
    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'style': 'width: 100%; padding: 0.375rem 0.75rem; font-size: 1rem; line-height: 1.5; color: #495057; background-color: #fff; background-clip: padding-box; border: 1px solid #ced4da; border-radius: 0.25rem; transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;'
        })
    )

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']

    def clean_number_of_seats(self):
        number_of_seats = self.cleaned_data['number_of_seats']
        if number_of_seats <= 0:
            raise forms.ValidationError("Number of seats must be greater than zero.")
        return number_of_seats