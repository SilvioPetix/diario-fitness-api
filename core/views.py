from rest_framework import viewsets, permissions,generics,status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Allenamento, DiarioAlimentare, BenessereGiornaliero, Misurazione
from .serializers import (
    AllenamentoSerializer,
    DiarioAlimentareSerializer,
    BenessereGiornalieroSerializer,
    MisurazioneSerializer,
)

# View per registrazione utente
class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username e password sono obbligatori."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username già in uso."}, status=status.HTTP_400_BAD_REQUEST)

        # Validazione password
        try:
            validate_password(password)
        except ValidationError as e:
            return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        # Creazione utente senza email
        user = User.objects.create_user(username=username, password=password)

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Registrazione avvenuta con successo."
        }, status=status.HTTP_201_CREATED)

# View per logout con blacklist refresh token
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout effettuato con successo."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Token non valido o mancante."}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class BasePublicViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]  # Accesso aperto a tutti

    def get_queryset(self):
        return self.queryset.filter(user = self.request.user)  # Ritorna tutti gli oggetti senza filtro

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
