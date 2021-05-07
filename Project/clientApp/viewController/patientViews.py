from django.shortcuts import render

# Create your views here.

# booking table
def allowed_bookings(request):
    return render(request, 'patient/bookings/bookings-table.html')

