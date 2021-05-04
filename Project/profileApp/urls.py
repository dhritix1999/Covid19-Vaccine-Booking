from django.urls import path

from .api.industryApi import industry_without_id, industry_with_id
from .api.patientApi import *
from .api.adminApi import *
from .api.medicalIssueApi import *

urlpatterns = [
    path('patient/login/', patient_login, name='patient_login'),
    path('patient/', patient_without_id, name='patient_without_id'),
    path('patient/<int:pk>/', patient_with_id, name='patient_with_id'),
    path('patient/<int:pk>/medical-issue', patients_medical_issues_without_id, name='patients_medical_issues_without_id'),
    path('patient/<int:patient_pk>/medical-issue/<int:medical_issue_pk>/', patients_medical_issues_with_id, name='patients_medical_issues_with_id'),

    path('admin/login/', admin_login, name='admin_login'),
    path('admin/', admin_without_id, name='admin_without_id'),
    path('admin/<int:pk>/', admin_with_id, name='admin_with_id'),

    path('medical-issue/', medical_issue_without_id, name='medical_issue_without_id'),
    path('medical-issue/<int:pk>/', medical_issue_with_id, name='medical_issue_with_id'),

    path('industry/', industry_without_id, name='industry_without_id'),
    path('industry/<int:pk>/', industry_with_id, name='industry_with_id'),

]
