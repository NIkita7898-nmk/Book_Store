from .serializer import InformationSerializer,InformationHistorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Information
# Create your views here.

class InformationView(ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer

class InformationHistoryView(RetrieveAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationHistorySerializer
