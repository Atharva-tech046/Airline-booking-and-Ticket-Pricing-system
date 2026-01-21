from django.contrib import admin
from .models import Airport, Flight, Seat, Booking, PricingRule

# Register your models here
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.register(PricingRule)