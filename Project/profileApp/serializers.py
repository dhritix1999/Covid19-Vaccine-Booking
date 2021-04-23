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
    # patientMedicalIssues = MedicalIssueSerializer(many=True)
    # industry = IndustrySerializer(read_only=True)
    patientMedicalIssues = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, queryset=MedicalIssue.objects.all())
    industry = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Industry.objects.all())


    class Meta:
        model = Patient
        fields = '__all__'

    # def create(self, validated_data):
    #     # We first remove the list of PKs because the database can't save this
    #     pksOfMedicalIssues = validated_data.pop('patientMedicalIssues')
    #     patient = Patient.objects.create(**validated_data)
    #
    #     for pkMedicalIssue in pksOfMedicalIssues:
    #         medicalIssue = MedicalIssue.objects.get(id=pkMedicalIssue["id"])
    #         patient.patientMedicalIssues.add(medicalIssue)
    #
    #     return patient

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
