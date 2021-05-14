from django.urls import path

from .api.industryApi import industry_without_id, industry_with_id
from .api.patientApi import *
from .api.adminApi import *
from .api.medicalIssueApi import *

urlpatterns = [
    path('patient/login/', patient_login, name='patient_login'),
    path('patients/', patient_without_id, name='patient_without_id'),
    path('patients/<int:pk>/', patient_with_id, name='patient_with_id'),
    path('patients/<int:pk>/medical-issues', patients_medical_issues_without_id, name='patients_medical_issues_without_id'),
    path('patients/<int:patient_pk>/medical-issues/<int:medical_issue_pk>/', patients_medical_issues_with_id, name='patients_medical_issues_with_id'),
    path('patients/<int:pk>/priorities', patient_priority, name='patient_priority'),

    path('admin/login/', admin_login, name='admin_login'),
    path('admins/', admin_without_id, name='admin_without_id'),
    path('admins/<int:pk>/', admin_with_id, name='admin_with_id'),

    path('medical-issues/', medical_issue_without_id, name='medical_issue_without_id'),
    path('medical-issues/<int:pk>/', medical_issue_with_id, name='medical_issue_with_id'),

    path('industries/', industry_without_id, name='industry_without_id'),
    path('industries/<int:pk>/', industry_with_id, name='industry_with_id'),

]
