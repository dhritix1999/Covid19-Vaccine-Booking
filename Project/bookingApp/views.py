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

    if request.method == 'GET':  # profileApp requesting data
        bookings = Booking.objects.filter(patientID=patient_pk)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'DELETE'])
def patient_booking_slot_with_id(request, patient_pk, booking_slot_pk):
    """
    Retrieve, update or delete a profileApp by id.
    """
    try:
        # Just check for existency of booking slot (cannot do for patient, diff microservice)
        _ = BookingSlot.objects.get(id=booking_slot_pk)
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
        return Response(status=status.HTTP_200_OK)


    elif request.method == 'DELETE':
        try:
            booking = Booking.objects.get(bookingSlotID=booking_slot_pk, patientID=patient_pk)
            booking.delete()
            return Response(status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)