from rest_framework import serializers
from .models import Allenamento, DiarioAlimentare, BenessereGiornaliero, Misurazione

class AllenamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allenamento
        fields = '__all__'

class DiarioAlimentareSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiarioAlimentare
        fields = '__all__'

class BenessereGiornalieroSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenessereGiornaliero
        fields = '__all__'

class MisurazioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Misurazione
        fields = '__all__'
        read_only_fields = ('bmi_valore', 'bmi_descr', 'bfm')  # campi calcolati readonly
