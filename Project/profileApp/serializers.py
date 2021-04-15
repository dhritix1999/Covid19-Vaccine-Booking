from rest_framework import serializers
from .models import Patient, MedicalIssue, Admin


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

    # def create(self, validated_data):
    #     return Patient.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)


class PatientLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id',)


class MedicalIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalIssue
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id',)
