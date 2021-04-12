from rest_framework import serializers
from .models import Patient, MedicalIssue


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    # def create(self, validated_data):
    #     return Patient.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)


class MedicalIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalIssue
        fields = '__all__'


