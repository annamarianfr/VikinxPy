from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Clinics
from .serializers import ClinicsSerializer
# Create your views here.

class ClinicsViewSet(viewsets.ModelViewSet):
    queryset = Clinics.objects.all()
    serializer_class = ClinicsSerializer


class ClinicsListView(APIView):
    queryset = Clinics.objects.all()

    def get(self, request, format=None):
        questions = []
        for question in Clinics.objects.all():
            serilizer = ClinicsSerializer(
                question, context={'request': request})
            questions.append(serilizer.data)
        return Response(questions)