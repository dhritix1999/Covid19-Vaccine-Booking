from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from bookingApp.models import BookingSlot
from bookingApp.serializers import BookingSlotSerializer


@api_view(['GET', 'POST'])
def booking_slot_without_id(request):
    """
    Retrieve all patients or create new patient
    """
    if request.method == 'GET':  # patient requesting data
        bookingSlots = BookingSlot.objects.all()
        serializer = BookingSlotSerializer(bookingSlots, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # patient creating data
        serializer = BookingSlotSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def booking_slot_with_id(request, pk):
    """
    Retrieve, update or delete a patient by id.
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
