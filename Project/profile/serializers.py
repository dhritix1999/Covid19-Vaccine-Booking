from rest_framework import serializers
from .models import Patient, Admin


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

# class PatientSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     phone = serializers.CharField(max_length=15, unique=True)
#     email = serializers.EmailField(unique=True)
#     password = serializers.CharField(max_length=100)
#     dateOfBirth = serializers.DateField()
#     gender = serializers.CharField(max_length=6)
#     emiratesID = serializers.IntegerField(max=999999999999999)
#     industry = serializers.CharField(max_length=100)
#     locationLat = serializers.FloatField()
#     locationLng = serializers.FloatField()
#     determination = serializers.BooleanField(default=False)
#     dosesTaken = serializers.IntegerField(default=0, max=2)


# def create(self, validated_data):
#     return Patient.objects.create(validated_data)
#
# def update(self, instance, validated_data):
#     instance.email = validated_data.get('email', instance.email)
