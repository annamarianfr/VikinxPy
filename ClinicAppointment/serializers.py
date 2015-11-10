from rest_framework import serializers

from .models import Clinics


class ClinicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinics
        fields = ('id', 'name', 'lati','longi')