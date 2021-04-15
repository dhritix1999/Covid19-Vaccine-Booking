import json
from profileApp.models import Admin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from profileApp.serializers import AdminSerializer, AdminLoginSerializer


@api_view(['POST'])
def admin_login(request):
    """
        Retrieve id of admin if they are in the system
    """
    try:
        data = json.loads(request.body)
        login = Admin.objects.get(email=data['email'], password=data['password'])
    except Admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = AdminLoginSerializer(login)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def admin_without_id(request):
    """
    Retrieve all Admins or create new Admin
    """
    if request.method == 'GET':  # Admin requesting data
        admins = Admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # Admin creating data
        serializer = AdminSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def admin_with_id(request, pk):
    """
    Retrieve, update or delete a Admin by id.
    """
    try:
        admin = Admin.objects.get(pk=pk)
    except Admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminSerializer(admin)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdminSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        admin.delete()
        return Response(status=status.HTTP_200_OK)
