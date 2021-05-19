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

    # medical issues
    path('admins/medical-issues', adminsViews.medical_issues_list),
    path('admins/medical-issues/add', adminsViews.medical_add_medical_issue),
    path('admins/medical-issues/<int:pk>/edit', adminsViews.medical_edit_medical_issue),

    # vaccine centers
    path('admins/vaccine-centers', adminsViews.vaccine_centers_list),
    path('admins/vaccine-centers/add', adminsViews.add_vaccine_center),
    path('admins/vaccine-centers/<int:pk>/edit', adminsViews.edit_vaccine_center),

    #logout
    path('logout', authenticationViews.logout),


]
