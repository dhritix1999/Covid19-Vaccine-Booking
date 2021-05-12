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
    path('patient/booking/start', patientViews.start_booking),
    path('patient/booking/vaccine-center', patientViews.vaccine_centres),
    path('patient/booking/vaccine-center/<int:pk>/slots', patientViews.booking_slots),

    path('patient/booking/history', patientViews.booking_history),

    # industry
    path('admins/industry', authenticationViews.industry_list),
    path('admins/industry/add', authenticationViews.add_industry),
    path('admins/industry/<int:pk>/edit', authenticationViews.edit_industry),


    # priority


    # vaccine centers




]
