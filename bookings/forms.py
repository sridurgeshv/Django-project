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
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_seats']

    def clean_number_of_seats(self):
        number_of_seats = self.cleaned_data['number_of_seats']
        if number_of_seats <= 0:
            raise forms.ValidationError("Number of seats must be greater than zero.")
        return number_of_seats