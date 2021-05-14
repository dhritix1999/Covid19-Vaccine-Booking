from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from vaccineCenterApp.models import VaccineCenter
from vaccineCenterApp.serializers import VaccineCenterSerializer
import requests
import json
import math

@api_view(['GET', 'POST'])
def vaccine_center_without_id(request):
    """
    Retrieve all patients or create new profileApp
    """
    if request.method == 'GET':  # profileApp requesting data
        vaccineCenters = VaccineCenter.objects.all()
        serializer = VaccineCenterSerializer(vaccineCenters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # profileApp creating data
        serializer = VaccineCenterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def vaccine_center_with_id(request, pk):
    """
    Retrieve, update or delete a profileApp by id.
    """
    try:
        vaccineCenter = VaccineCenter.objects.get(pk=pk)
    except VaccineCenter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VaccineCenterSerializer(vaccineCenter)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VaccineCenterSerializer(vaccineCenter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vaccineCenter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def patient_possible_vaccine_centers(request, patient_pk):
    """
    Get all vaccine centers for a given patient to possibly book at
    """
    if request.method == 'GET':
        isPriority = request.query_params.get('is_priority') == 'true'

        # Get patient info from Patients Microservice
        r=requests.get(f'http://127.0.0.1:8000/api/patients/{patient_pk}/')

        if r.status_code >= 400:
            return Response(status=status.HTTP_404_NOT_FOUND)

        patient = r.json()

        # Non-priority patients can only book if doses < 100, all patients need > 0
        if isPriority:
            centers = VaccineCenter.objects.filter(dosesStock__gt=0)
        else:
            centers = VaccineCenter.objects.filter(dosesStock__gt=100)

        # Sort the vaccine centers based on distance from user
        centers = list(centers)
        centers.sort(key=lambda x: math.sqrt((patient['locationLat'] - x.locationLat)**2 + (patient['locationLng'] - x.locationLng)**2))

        serializer = VaccineCenterSerializer(centers, many=True)
        return Response(serializer.data)
