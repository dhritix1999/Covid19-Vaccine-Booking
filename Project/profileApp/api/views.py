from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Project.profileApp.models import Patient, MedicalIssue
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from Project.profileApp.serializers import PatientSerializer, MedicalIssueSerializer


def register(request):
    return render(request, 'register.html')


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
        return Response(status=status.HTTP_204_NO_CONTENT)

### Medical Issues

@api_view(['GET', 'POST'])
def medical_issue_without_id(request):
    """
    Retrieve all patients or create new profileApp
    """
    if request.method == 'GET':  # profileApp requesting data
        medicalIssue = MedicalIssue.objects.all()
        serializer = MedicalIssueSerializer(medicalIssue, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # profileApp creating data
        serializer = MedicalIssueSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def medical_issue_with_id(request, pk):
    """
    Retrieve, update or delete a profileApp by id.
    """
    try:
        medicalIssue = MedicalIssue.objects.get(pk=pk)
    except MedicalIssue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MedicalIssueSerializer(medicalIssue)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MedicalIssueSerializer(medicalIssue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        medicalIssue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
