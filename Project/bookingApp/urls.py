from django.urls import  path
from . import views
from .views import booking_slot_without_id, booking_slot_with_id, patient_booking_slot_with_id, \
    patient_booking_slot_without_id, booking_slot_patient_without_id, vaccine_center_bookings

urlpatterns = [
    path('api/booking-slots/', booking_slot_without_id, name='booking_slot_without_id'),
    path('api/booking-slots/<int:pk>/', booking_slot_with_id, name='booking_slot_with_id'),

    path('api/patients/<int:patient_pk>/booking-slots/', patient_booking_slot_without_id, name='patient_booking_slot_without_id'),
    path('api/patients/<int:patient_pk>/booking-slots/<int:booking_slot_pk>/', patient_booking_slot_with_id, name='patient_booking_slot_with_id'),

    path('api/booking-slots/<int:booking_slot_pk>/patients/', booking_slot_patient_without_id, name='booking_slot_patient_without_id'),

    # flag: is_available=true/false
    path('api/patients/<int:patient_pk>/vaccine-centers/<int:vaccine_center_pk>/booking-slots/', vaccine_center_bookings,name='vaccine_center_bookings'),


]
