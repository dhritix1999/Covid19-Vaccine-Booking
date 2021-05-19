from django.urls import path
from .viewController import authenticationViews, patientViews, adminsViews

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
    path('admins/industry', adminsViews.industry_list),
    path('admins/industry/add', adminsViews.add_industry),
    path('admins/industry/<int:pk>/edit', adminsViews.edit_industry),


    # priority


    # vaccine centers
    path('admins/vaccine-centers', adminsViews.vaccine_centers_list),
    path('admins/vaccine-centers/add', adminsViews.add_vaccine_center),
    path('admins/vaccine-centers/<int:pk>/edit', adminsViews.edit_vaccine_center)


]
