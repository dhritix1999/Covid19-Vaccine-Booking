from rest_framework import serializers
from .models import Patient, MedicalIssue, Admin, Industry


class MedicalIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalIssue
        fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    # patientMedicalIssues = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, queryset=MedicalIssue.objects.all())
    patientMedicalIssues = MedicalIssueSerializer(many=True, read_only=True)
    
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

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id',)
