from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .models import Allenamento, DiarioAlimentare, BenessereGiornaliero, Misurazione
from .serializers import (
    AllenamentoSerializer,
    DiarioAlimentareSerializer,
    BenessereGiornalieroSerializer,
    MisurazioneSerializer,
)

class BaseUserOnlyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = User.objects.get(username='asus')  # attenzione: alza errore se l'utente non esiste
        return self.queryset.filter(user=user)

# Allenamento
class AllenamentoViewSet(BaseUserOnlyViewSet):
    queryset = Allenamento.objects.all().order_by('id')
    serializer_class = AllenamentoSerializer



# Diario Alimentare
class DiarioAlimentareViewSet(BaseUserOnlyViewSet):
    queryset = DiarioAlimentare.objects.all().order_by('id')
    serializer_class = DiarioAlimentareSerializer

# Benessere Giornaliero
class BenessereGiornalieroViewSet(BaseUserOnlyViewSet):
    queryset = BenessereGiornaliero.objects.all().order_by('id')
    serializer_class = BenessereGiornalieroSerializer

# Misurazione
class MisurazioneViewSet(BaseUserOnlyViewSet):
    queryset = Misurazione.objects.all().order_by('id')
    serializer_class = MisurazioneSerializer
