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
    context = {"view_profile": True}
    return render(request, 'patient/view-edit-profile.html', context)


def update_profile(request):
    context = {"view_profile": False}
    return render(request, 'patient/view-edit-profile.html', context)
