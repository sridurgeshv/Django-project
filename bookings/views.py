from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TravelOption, Booking
from .forms import UserRegistrationForm, TravelFilterForm, BookingForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'bookings/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'bookings/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'bookings/login.html', {'form': form})

@login_required
def travel_list(request):
    form = TravelFilterForm(request.GET)
    travel_options = TravelOption.objects.all()
    
    if form.is_valid():
        if form.cleaned_data['type']:
            travel_options = travel_options.filter(type=form.cleaned_data['type'])
        if form.cleaned_data['source']:
            travel_options = travel_options.filter(source__icontains=form.cleaned_data['source'])
        if form.cleaned_data['destination']:
            travel_options = travel_options.filter(destination__icontains=form.cleaned_data['destination'])
        if form.cleaned_data['date']:
            travel_options = travel_options.filter(date_time__date=form.cleaned_data['date'])

    return render(request, 'bookings/travel_list.html', {'travel_options': travel_options, 'form': form})

@login_required
def booking_form(request, travel_id):
    travel_option = get_object_or_404(TravelOption, pk=travel_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel_option
            booking.total_price = travel_option.price * booking.number_of_seats
            booking.save()
            
            # Update available seats
            travel_option.available_seats -= booking.number_of_seats
            travel_option.save()
            
            messages.success(request, 'Booking confirmed successfully!')
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form, 'travel_option': travel_option})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if request.method == 'POST':
        booking.status = 'CANCELLED'
        booking.save()
        
        # Restore available seats
        travel_option = booking.travel_option
        travel_option.available_seats += booking.number_of_seats
        travel_option.save()
        
        messages.success(request, 'Booking cancelled successfully!')
    return redirect('booking_list')