from django.urls import  path
from . import views
from .views import booking_slot_without_id, booking_slot_with_id

urlpatterns = [
    path('api/booking-slot/', booking_slot_without_id, name='booking_slot_without_id'),
    path('api/booking-slot/<int:pk>/', booking_slot_with_id, name='booking_slot_with_id'),
]
