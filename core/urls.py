from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'allenamenti', AllenamentoViewSet)
router.register(r'diario', DiarioAlimentareViewSet)
router.register(r'benessere', BenessereGiornalieroViewSet)
router.register(r'misurazioni', MisurazioneViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
