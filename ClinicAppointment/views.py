from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Clinic,Appointment
from .serializers import ClinicSerializer,AppointmentSerializer
# Create your views here.

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer


class ClinicListView(APIView):
    queryset = Clinic.objects.all()

    def get(self, request, format=None):
        questions = []
        for question in Clinic.objects.all():
            serilizer = ClinicSerializer(
                question, context={'request': request})
            questions.append(serilizer.data)
        return Response(questions)
    def post(self, request, format=None):
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentListView(APIView):
    queryset = Appointment.objects.all()

    def get(self, request, format=None):
        questions = []
        for question in Appointment.objects.all():
            serilizer = AppointmentSerializer(
                question, context={'request': request})
            questions.append(serilizer.data)
        return Response(questions)
    def post(self, request, format=None):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        