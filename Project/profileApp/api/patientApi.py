import json
from profileApp.models import Patient
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profileApp.serializers import PatientSerializer, PatientLoginSerializer


@api_view(['POST'])
def patient_login(request):
    """
        Retrieve id of patient if they are in the system
    """
    try:
        data = json.loads(request.body)
        login = Patient.objects.get(email=data['email'], password=data['password'])
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = PatientLoginSerializer(login)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def patient_without_id(request):
    """
    Retrieve all patients or create new profileApp
    """
    if request.method == 'GET':  # profileApp requesting data
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # profileApp creating data
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def patient_with_id(request, pk):
    """
    Retrieve, update or delete a profileApp by id.
    """
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_200_OK)
