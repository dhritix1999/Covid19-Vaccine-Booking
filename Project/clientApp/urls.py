from django.urls import path
from .viewController import authenticationViews, patientViews

urlpatterns = [

    path('', authenticationViews.index),
    path('register', authenticationViews.patient_register),
    path('admins', authenticationViews.admin_homepage),
    path('patient', authenticationViews.patient_homepage),

    path('patient/booking/list', patientViews.allowed_bookings),



]