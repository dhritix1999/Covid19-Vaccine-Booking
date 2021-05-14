import datetime

import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from bookingApp.models import BookingSlot, Booking
from bookingApp.serializers import BookingSlotSerializer, BookingSerializer


@api_view(['GET', 'POST'])
def booking_slot_without_id(request):
    """
    Retrieve all patients or create new profileApp
    """
    if request.method == 'GET':  # profileApp requesting data
        bookingSlots = BookingSlot.objects.all()
        serializer = BookingSlotSerializer(bookingSlots, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # profileApp creating data
        serializer = BookingSlotSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def booking_slot_with_id(request, pk):
    """
    Retrieve, update or delete a profileApp by id.
    """
    try:
        bookingSlot = BookingSlot.objects.get(pk=pk)
    except BookingSlot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookingSlotSerializer(bookingSlot)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookingSlotSerializer(bookingSlot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bookingSlot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def patient_booking_slot_without_id(request, patient_pk):
    """
        Get all bookings of patient
    """
    if request.method == 'GET':  # profileApp requesting data
        bookings = Booking.objects.filter(patientID=patient_pk)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def booking_slot_patient_without_id(request, booking_slot_pk):
    """
        Get all patients of booking slot
    """
    if request.method == 'GET':  # profileApp requesting data
        bookings = Booking.objects.filter(bookingSlotID=booking_slot_pk)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST', 'DELETE'])
def patient_booking_slot_with_id(request, patient_pk, booking_slot_pk):
    """
    Retrieve, update or delete a booking slot of patient
    """
    try:
        bookingSlot = BookingSlot.objects.get(id=booking_slot_pk)
    except BookingSlot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            booking = Booking.objects.get(bookingSlotID=booking_slot_pk, patientID=patient_pk)
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        Booking.objects.create(bookingSlotID=booking_slot_pk, patientID=patient_pk)

        # Also increment booking
        bookingSlot.bookingCount += 1
        bookingSlot.save()

        return Response(status=status.HTTP_200_OK)


    elif request.method == 'DELETE':
        try:
            booking = Booking.objects.get(bookingSlotID=booking_slot_pk, patientID=patient_pk)
            booking.delete()
            return Response(status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def vaccine_center_bookings(request, patient_pk, vaccine_center_pk):
    """
    Get all available/unavailable booking slots for a vaccine center
    query_params = "is_available": true or false
    """
    if request.method == 'GET':
        isAvailable = request.query_params.get('is_available') == 'true'

        # Get vaccine center info from VaccineCenter Microservice
        r=requests.get(f'http://127.0.0.1:8000/api/vaccine-centers/{vaccine_center_pk}')

        if r.status_code >= 400:
            return Response(status=status.HTTP_404_NOT_FOUND)

        vaccineCenter = r.json()

        # Get patient Priority from Patient Microservice
        r=requests.get(f'http://127.0.0.1:8000/api/patients/{patient_pk}/priorities')

        if r.status_code >= 400:
            return Response(status=status.HTTP_404_NOT_FOUND)

        patientPriority = r.json()
        isPriority = patientPriority['priority']

        print(isPriority)

        # If patient is not priority, only booking slots with < 75% booked capacity are available
        if isPriority:
            bookingCountLimit = vaccineCenter['dosesPerHour']
        else:
            bookingCountLimit = int(0.75 * vaccineCenter['dosesPerHour'])

        print(bookingCountLimit)
        
        # Filter slots within the next 3 days
        # Filter slots below capacity / at capacity depending on isAvailable or not
        if isAvailable:
            slots = BookingSlot.objects.filter(
                timeSlot__gte=datetime.datetime.now(),
                bookingCount__lt=bookingCountLimit
            )
        else:
            slots = BookingSlot.objects.filter(
                timeSlot__gte=datetime.datetime.now(),
                bookingCount__gte=bookingCountLimit
            )


        ### ALT BEHAVIOR IF DATE SPECIFIED
        ### DATE FORMAT EXAMPLE: 2021-05-15T17:00:00
        filteredDateString = request.query_params.get('filtered_date')
        if filteredDateString != None:
            filteredDate = datetime.datetime.strptime(filteredDateString, '%Y-%m-%dT%H:%M:%S')
            slots = slots.filter(timeSlot__year=filteredDate.year, timeSlot__month=filteredDate.month, timeSlot__day=filteredDate.day, timeSlot__hour=filteredDate.hour)

        serializer = BookingSlotSerializer(slots, many=True)
        return Response(serializer.data)
