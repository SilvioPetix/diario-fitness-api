from rest_framework import viewsets, permissions
from .models import Allenamento, DiarioAlimentare, BenessereGiornaliero, Misurazione
from .serializers import (
    AllenamentoSerializer,
    DiarioAlimentareSerializer,
    BenessereGiornalieroSerializer,
    MisurazioneSerializer,
)

class BasePublicViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]  # Accesso aperto a tutti

    def get_queryset(self):
        return self.queryset.all()  # Ritorna tutti gli oggetti senza filtro

class AllenamentoViewSet(BasePublicViewSet):
    queryset = Allenamento.objects.all().order_by('id')
    serializer_class = AllenamentoSerializer

class DiarioAlimentareViewSet(BasePublicViewSet):
    queryset = DiarioAlimentare.objects.all().order_by('id')
    serializer_class = DiarioAlimentareSerializer

class BenessereGiornalieroViewSet(BasePublicViewSet):
    queryset = BenessereGiornaliero.objects.all().order_by('id')
    serializer_class = BenessereGiornalieroSerializer

class MisurazioneViewSet(BasePublicViewSet):
    queryset = Misurazione.objects.all().order_by('id')
    serializer_class = MisurazioneSerializer
