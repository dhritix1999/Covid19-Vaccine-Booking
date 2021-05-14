from django.urls import  path
from .views import vaccine_center_without_id, vaccine_center_with_id, patient_possible_vaccine_centers

urlpatterns = [
    path('api/vaccine-centers/', vaccine_center_without_id, name='vaccine_center_without_id'),
    path('api/vaccine-centers/<int:pk>/', vaccine_center_with_id, name='vaccine_center_with_id'),

    path('api/patients/<int:patient_pk>/vaccine-centers/', patient_possible_vaccine_centers, name='patient_possible_vaccine_centers'),

]
