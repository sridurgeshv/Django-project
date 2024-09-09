from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TravelOption, Booking

class TravelOptionModelTest(TestCase):
    def test_travel_option_creation(self):
        travel_option = TravelOption.objects.create(
            travel_type='Flight',
            source='New York',
            destination='London',
            price=500,
            available_seats=100
        )
        self.assertTrue(isinstance(travel_option, TravelOption))
        self.assertEqual(travel_option.__str__(), f"{travel_option.travel_type} from {travel_option.source} to {travel_option.destination}")

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.travel_option = TravelOption.objects.create(
            travel_type='Flight',
            source='New York',
            destination='London',
            price=500,
            available_seats=100
        )

    def test_booking_creation(self):
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel_option,
            number_of_seats=2,
            total_price=1000
        )
        self.assertTrue(isinstance(booking, Booking))
        self.assertEqual(booking.__str__(), f"Booking {booking.id} by {self.user.username}")

class ViewsTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/home.html')

    def test_travel_list_view(self):
        response = self.client.get(reverse('travel_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/travel_list.html')