from rest_framework import serializers

from vaccineCenterApp.models import VaccineCenter


class VaccineCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineCenter
        fields = '__all__'

