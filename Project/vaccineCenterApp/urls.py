from django.urls import  path
from .views import vaccine_center_without_id, vaccine_center_with_id, patient_possible_vaccine_centers

urlpatterns = [
    path('api/vaccine-center/', vaccine_center_without_id, name='vaccine_center_without_id'),
    path('api/vaccine-center/<int:pk>/', vaccine_center_with_id, name='vaccine_center_with_id'),

    path('api/patient/<int:patient_pk>/vaccine-center/', patient_possible_vaccine_centers, name='patient_possible_vaccine_centers'),

]
