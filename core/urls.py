from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LogoutView

router = DefaultRouter()
router.register(r'allenamenti', AllenamentoViewSet)
router.register(r'diario', DiarioAlimentareViewSet)
router.register(r'benessere', BenessereGiornalieroViewSet)
router.register(r'misurazioni', MisurazioneViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # JWT Auth endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Custom auth endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
