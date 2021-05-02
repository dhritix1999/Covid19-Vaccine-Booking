from django.urls import  path
from . import views
from .views import booking_slot_without_id, booking_slot_with_id, patient_booking_slot_with_id, \
    patient_booking_slot_without_id, booking_slot_patient_without_id, vaccine_center_bookings

urlpatterns = [
    path('api/booking-slot/', booking_slot_without_id, name='booking_slot_without_id'),
    path('api/booking-slot/<int:pk>/', booking_slot_with_id, name='booking_slot_with_id'),

    path('api/patient/<int:patient_pk>/booking-slot/', patient_booking_slot_without_id, name='patient_booking_slot_without_id'),
    path('api/patient/<int:patient_pk>/booking-slot/<int:booking_slot_pk>/', patient_booking_slot_with_id, name='patient_booking_slot_with_id'),

    path('api/booking-slot/<int:booking_slot_pk>/patient/', booking_slot_patient_without_id, name='booking_slot_patient_without_id'),

    path('api/vaccine-center/<int:vaccine_center_pk>/booking-slot/', vaccine_center_bookings,name='vaccine_center_bookings'),


]
