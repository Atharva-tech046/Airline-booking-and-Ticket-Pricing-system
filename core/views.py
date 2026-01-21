from django.shortcuts import render
from django.http import JsonResponse
from .models import Flight

# 1. The Homepage View (New!)
def home(request):
    return render(request, 'core/index.html')

# 2. The API View (Already exists)
def search_flights(request):
    origin_code = request.GET.get('origin')
    destination_code = request.GET.get('destination')

    if origin_code and destination_code:
        flights = Flight.objects.filter(
            origin__code=origin_code, 
            destination__code=destination_code
        )
    else:
        flights = Flight.objects.none()

    data = []
    for flight in flights:
        data.append({
            "id": flight.id,
            "origin": flight.origin.code,
            "destination": flight.destination.code,
            "departure": flight.departure.strftime("%Y-%m-%d %H:%M"),
            "base_price": float(flight.base_price),
            "final_price": float(flight.get_dynamic_price())
        })

    return JsonResponse(data, safe=False)