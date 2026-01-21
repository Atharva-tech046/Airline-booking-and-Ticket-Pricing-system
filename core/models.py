from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    
class PricingRule(models.Model):
    name = models.CharField(max_length=50) 
    min_days_before = models.IntegerField()
    max_days_before = models.IntegerField()
    price_multiplier = models.DecimalField(max_digits=3, decimal_places=2)

class Flight(models.Model):
    origin = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='arrivals')
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.origin.code} -> {self.destination.code}"

    def get_dynamic_price(self):
        from decimal import Decimal
        from django.utils import timezone
        price = self.base_price
        days_until = (self.departure - timezone.now()).days
        if days_until < 7:
            price = price * Decimal("1.5")
        return price

def get_dynamic_price(self):
        days_diff = (self.departure_time.date() - date.today()).days
        
        rule = PricingRule.objects.filter(
            min_days_before__lte=days_diff,
            max_days_before__gte=days_diff
        ).first()

        multiplier = rule.price_multiplier if rule else 1.0
        return round(self.base_price * multiplier, 2)

class Seat(models.Model):
    SEAT_CLASSES = [('E', 'Economy'), ('B', 'Business')]
    
    # These were likely missing or misspelled in your file:
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="seats")
    row_number = models.IntegerField()
    seat_letter = models.CharField(max_length=1)
    seat_class = models.CharField(max_length=1, choices=SEAT_CLASSES, default='E')
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('flight', 'row_number', 'seat_letter')

    def __str__(self):
        return f"Row {self.row_number}{self.seat_letter}"

# 5. BOOKING - The transaction receipt
class Booking(models.Model):
    # Notice there are NO parentheses after models.CASCADE
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE) 
    booking_date = models.DateTimeField(auto_now_add=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.id} - {self.user.username}"
