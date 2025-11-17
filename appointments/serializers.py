# DRF serializer’lar

from rest_framework import serializers
from .models import Patient, Provider, Appointment


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    provider = ProviderSerializer(read_only=True)

    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source='patient', write_only=True
    )
    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=Provider.objects.all(), source='provider', write_only=True
    )

    class Meta:
        model = Appointment
        fields = [
            'id',
            'patient',
            'provider',
            'patient_id',
            'provider_id',
            'appointment_time',
            'duration_minutes',
            'status',
            'notes',
        ]
