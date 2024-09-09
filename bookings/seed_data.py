import os
import sys
import django

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_booking.settings')
django.setup()

# Rest of your script remains the same
from bookings.models import TravelOption
import random
from datetime import datetime, timedelta

def create_sample_travel_options():
    # Clear existing data
    TravelOption.objects.all().delete()

    travel_types = ['FLIGHT', 'TRAIN', 'BUS']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
              'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

    for _ in range(50):  # Create 50 sample travel options
        travel_type = random.choice(travel_types)
        source, destination = random.sample(cities, 2)
        date_time = datetime.now() + timedelta(days=random.randint(1, 30))
        price = round(random.uniform(50, 500), 2)
        available_seats = random.randint(1, 100)

        TravelOption.objects.create(
            type=travel_type,
            source=source,
            destination=destination,
            date_time=date_time,
            price=price,
            available_seats=available_seats
        )

    print(f"Created {TravelOption.objects.count()} sample travel options.")

if __name__ == '__main__':
    create_sample_travel_options()
