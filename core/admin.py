from django.contrib import admin
from .models import Allenamento, DiarioAlimentare, Misurazione, BenessereGiornaliero, UserProfile

@admin.register(Allenamento)
class AllenamentiAdmin(admin.ModelAdmin):
    list_display = ['user', 'data', 'giorno', 'esercizio_display', 'serie', 'ripetizioni', 'peso', 'note']
    list_filter = ['giorno', 'data']
    search_fields = ['user__username', 'esercizio']
    date_hierarchy = 'data'
    ordering = ['-data']

    def esercizio_display(self, obj):
        return f"{obj.esercizio or ''} ({obj.serie}x{obj.ripetizioni} @ {obj.peso}kg)"
    esercizio_display.short_description = 'Dettaglio esercizio'

@admin.register(DiarioAlimentare)
class DiarioAlimentareAdmin(admin.ModelAdmin):
    list_display = ['user', 'data', 'tipologia_pasto', 'descrizione']
    list_filter = ['data']
    search_fields = ['user__username', 'tipologia_pasto', 'descrizione']
    date_hierarchy = 'data'
    ordering = ['-data']

@admin.register(BenessereGiornaliero)
class BenessereGiornalieroAdmin(admin.ModelAdmin):
    list_display = ['user', 'data', 'acqua_litri', 'sigarette_fumate', 'note']
    list_filter = ['data']
    search_fields = ['user__username']
    date_hierarchy = 'data'
    ordering = ['-data']

@admin.register(Misurazione)
class MisurazioneAdmin(admin.ModelAdmin):
    list_display = ['user', 'data', 'peso_kg', 'bmi_display', 'bmi_descr', 'bfm_display']
    list_filter = ['data']
    search_fields = ['user__username']
    date_hierarchy = 'data'
    ordering = ['-data']
    readonly_fields = ['bmi_valore', 'bmi_descr', 'bfm']

    def get_fields(self, request, obj=None):
        base_fields = [
            'user', 'data', 'peso_kg', 'vita_cm', 'collo_cm', 'fianchi_cm', 'note'
        ]
        if obj:
            base_fields += ['bmi_valore', 'bmi_descr', 'bfm']
        return base_fields

    def bmi_display(self, obj):
        return round(obj.bmi_valore, 2) if obj.bmi_valore else "-"
    bmi_display.short_description = 'BMI'

    def bfm_display(self, obj):
        return f"{obj.bfm}%" if obj.bfm is not None else "-"
    bfm_display.short_description = 'BFM %'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'sesso', 'altezza']
    search_fields = ['user__username']
