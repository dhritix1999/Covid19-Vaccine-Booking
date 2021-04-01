from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Patient
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import PatientSerializer


def register(request):
    return render(request, 'register.html')


@api_view(['GET', 'POST'])
def patient(request):
    if request.method == 'GET':  # patient requesting data
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # patient creating data
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
