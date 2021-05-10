import json
from profileApp.models import Patient, MedicalIssue
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profileApp.serializers import PatientSerializer, PatientLoginSerializer, MedicalIssueSerializer


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


@api_view(['GET'])
def patients_medical_issues_without_id(request, pk):

    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # profileApp requesting data
        medicalIssues = patient.patientMedicalIssues.all()
        serializer = MedicalIssueSerializer(medicalIssues, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def patients_medical_issues_with_id(request, patient_pk, medical_issue_pk):
    """
    Retrieve, update or delete a profileApp by id.
    """
    try:
        patient = Patient.objects.get(pk=patient_pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            medicalIssue = patient.patientMedicalIssues.get(id=medical_issue_pk)
            serializer = MedicalIssueSerializer(medicalIssue)
            return Response(serializer.data)
        except MedicalIssue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'POST':
        try:
            unboundMedicalIssue = MedicalIssue.objects.get(id=medical_issue_pk)
            patient.patientMedicalIssues.add(unboundMedicalIssue)
            return Response(status=status.HTTP_200_OK)
        except MedicalIssue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'DELETE':
        try:
            medicalIssue = patient.patientMedicalIssues.get(id=medical_issue_pk)
            patient.patientMedicalIssues.remove(medicalIssue)
            return Response(status=status.HTTP_200_OK)
        except MedicalIssue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def patient_priority(request, pk):

    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':  # profileApp requesting data
        # Check if priority industry
        isPriority = patient.industry.priority if patient.industry != None else False
        # Check if person of determination
        isPriority = isPriority or patient.determination
        return Response({"priority": isPriority})