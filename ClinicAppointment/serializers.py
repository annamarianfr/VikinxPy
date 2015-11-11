from rest_framework import serializers

from .models import Clinic,Appointment


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment