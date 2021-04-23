from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from profileApp.models import Industry
from profileApp.serializers import IndustrySerializer


@api_view(['GET', 'POST'])
def industry_without_id(request):
    """
    Retrieve all industries or create new one
    """
    if request.method == 'GET':  # profileApp requesting data
        industry = Industry.objects.all()
        serializer = IndustrySerializer(industry, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # profileApp creating data
        serializer = IndustrySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)