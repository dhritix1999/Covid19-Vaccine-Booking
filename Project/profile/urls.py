from django.urls import path
from project.profile.views import patient_without_id, patient_with_id
from project.profile.api.adminUser import admin_without_id, admin_with_id

urlpatterns = [
    path('api/login/', login, name='login'),

    path('api/patient/', patient_without_id, name='patient_without_id'),
    path('api/patient/<int:pk>/', patient_with_id, name='patient_with_id'),

    path('api/admin/', admin_without_id, name='admin_without_id'),
    path('api/admin/<int:pk>/', admin_with_id, name='admin_with_id'),
]
