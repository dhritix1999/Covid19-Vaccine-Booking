from django.urls import  path
from . import views
from .views import patient_without_id, patient_with_id

urlpatterns = [
    path('register/', views.register, name='register'),
    path('api/patient/', patient_without_id, name='patient_without_id'),
    path('api/patient/<int:pk>/', patient_with_id, name='patient_with_id'),
]
