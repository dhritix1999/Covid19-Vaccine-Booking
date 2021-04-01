from django.urls import  path
from . import views
from .views import patient


urlpatterns = [
    path('register/', views.register, name='register'),
    path('api/patient/', patient, name='patients')

]
