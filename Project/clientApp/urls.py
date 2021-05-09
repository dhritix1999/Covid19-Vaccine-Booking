from django.urls import path
from .viewController import authenticationViews, patientViews

urlpatterns = [

    # authentication
    path('', authenticationViews.index),
    path('register', authenticationViews.patient_register),

    # homepage
    path('admins', authenticationViews.admin_homepage),
    path('patient', authenticationViews.patient_homepage),

    # patient profile
    path('patient/profile/view', patientViews.view_profile),
    path('patient/profile/update', patientViews.update_profile),

    # patient booking
    path('patient/booking/list', patientViews.allowed_bookings),
    path('patient/booking/start', patientViews.start_booking),
    path('patient/booking/history', patientViews.booking_history),

    # industry
    path('admins/industry', authenticationViews.admin_industry),

    # priority


    # vaccine centers




]
