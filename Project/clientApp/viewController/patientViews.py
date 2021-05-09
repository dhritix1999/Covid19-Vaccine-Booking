from django.shortcuts import render


# Create your views here.

# booking table
def allowed_bookings(request):
    return render(request, 'patient/bookings/bookings-table.html')


def start_booking(request):
    return None


def booking_history(request):
    return None


def view_profile(request):
    return render(request, 'patient/profile/view-profile.html')


def update_profile(request):
    return render(request, 'patient/profile/edit-profile.html')
