from django.shortcuts import render


# Create your views here.

# booking table
def start_booking(request):
    return render(request, 'patient/bookings/start-booking.html')


def vaccine_centres(request):
    return render(request, 'patient/bookings/centres-booking.html')


def booking_slots(request, pk):
    context = {"vaccineCenter": pk}
    return render(request, 'patient/bookings/bookings-table.html', context)


def booking_history(request):
    return render(request, 'patient/bookings/booking-history.html')


# user profile
def view_profile(request):
    context = {"view_profile": True}
    return render(request, 'patient/view-edit-profile.html', context)


def update_profile(request):
    context = {"view_profile": False}
    return render(request, 'patient/view-edit-profile.html', context)
