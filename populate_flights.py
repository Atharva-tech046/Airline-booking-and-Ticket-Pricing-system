import os
import django
import random
from datetime import datetime, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Flight, Airport

# Configuration
AIRPORT_CODES = ['JFK', 'LHR', 'DXB', 'BOM', 'DEL', 'TYO', 'CDG']

print("🚀 Step 1: Ensuring Airports exist...")

real_airports = []

for code in AIRPORT_CODES:
    obj, created = Airport.objects.get_or_create(code=code)
    real_airports.append(obj)
    if created:
        print(f"   - Created Airport: {code}")
    else:
        print(f"   - Found Airport: {code}")

print("\n🚀 Step 2: Generating 50 random flights...")

for i in range(50):
    origin_airport = random.choice(real_airports)
    destination_airport = random.choice(real_airports)
    
    while origin_airport == destination_airport:
        destination_airport = random.choice(real_airports)

    # Random Departure (next 30 days)
    random_days = random.randint(0, 30)
    departure_date = datetime.now() + timedelta(days=random_days)
    
    # 👇 THE FIX: Calculate Arrival (Departure + 2 to 10 hours)
    duration_hours = random.randint(2, 10)
    arrival_date = departure_date + timedelta(hours=duration_hours)
    
    price = random.randint(200, 1500)

    Flight.objects.create(
        origin=origin_airport,
        destination=destination_airport,
        departure=departure_date,
        arrival=arrival_date,  # <-- Added this!
        base_price=price
    )
    
    print(f"✅ Added: {origin_airport.code} -> {destination_airport.code}")

print("\n✨ DONE! Database successfully flooded.")