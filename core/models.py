from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
import math

# --- UserProfile ---
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    sesso = models.CharField(max_length=10, choices=[('M', 'Maschio'), ('F', 'Femmina')], blank=True, null=True)
    altezza = models.FloatField(blank=True, null=True)  # Altezza in cm
    immagine = models.ImageField(upload_to='profile_images/', blank=True, null=True, default='blank-profile-male.jpg')

    def __str__(self):
        return f"Profilo di {self.user.username}"

# --- Allenamento ---
class Allenamento(models.Model):
    GIORNI = [
        ('giorno1', 'Giorno 1'),
        ('giorno2', 'Giorno 2'),
        ('giorno3', 'Giorno 3'),
        ('giorno4', 'Giorno 4'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    giorno = models.CharField(max_length=10, choices=GIORNI)
    esercizio = models.CharField(max_length=20, null=True, blank=True)
    serie = models.PositiveIntegerField()
    ripetizioni = models.PositiveIntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso in kg")
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.giorno} - {self.data}"

    class Meta:
        verbose_name_plural = "Allenamenti"

# --- Diario Alimentare ---
class DiarioAlimentare(models.Model):
    TIPOLOGIE_PASTO = [
        ('colazione', 'Colazione'),
        ('spuntino_mattina', 'Spuntino Mattina'),
        ('pranzo', 'Pranzo'),
        ('spuntino_pomeriggio', 'Spuntino Pomeriggio'),
        ('cena', 'Cena'),
        ('spuntino_sera', 'Spuntino Sera'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    tipologia_pasto = models.CharField(max_length=20, choices=TIPOLOGIE_PASTO)
    descrizione = models.TextField(help_text="Cosa hai mangiato?")
    note = models.TextField(blank=True, help_text="Note aggiuntive (facoltative)")

    def __str__(self):
        return f"{self.user.username} - {self.tipologia_pasto} - {self.data}"

    class Meta:
        verbose_name_plural = "Diario Alimentare"

# --- Benessere Giornaliero ---
class BenessereGiornaliero(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(unique=True)
    acqua_litri = models.DecimalField(max_digits=4, decimal_places=2, help_text="Litri di acqua bevuti")
    sigarette_fumate = models.PositiveIntegerField(help_text="Numero di sigarette fumate", default=0)
    note = models.TextField(blank=True, help_text="Note personali")

    def __str__(self):
        return f"{self.user.username} - Benessere {self.data}"

    class Meta:
        verbose_name_plural = "Benessere Giornaliero"

# --- Misurazione ---
class Misurazione(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    vita_cm = models.PositiveIntegerField(help_text="Circonferenza vita (cm)")
    collo_cm = models.PositiveIntegerField(help_text="Circonferenza collo (cm)")
    fianchi_cm = models.PositiveIntegerField(null=True, blank=True, help_text="Solo per donne (cm)")
    note = models.TextField(blank=True)

    bmi_valore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    bmi_descr = models.CharField(max_length=20, null=True, blank=True)
    bfm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    @property
    def calcola_bmi(self):
        altezza_cm = self.user.profile.altezza
        if not altezza_cm:
            return None
        altezza_m = Decimal(altezza_cm) / Decimal('100')
        if altezza_m > 0:
            return float(self.peso_kg / (altezza_m ** 2))
        return None

    def calcola_descrizione_bmi(self, bmi):
        if bmi is None:
            return None
        if bmi < 18.5:
            return "Sottopeso"
        elif 18.5 <= bmi < 25:
            return "Normopeso"
        elif 25 <= bmi < 30:
            return "Sovrappeso"
        elif 30 <= bmi < 35:
            return "Obeso"
        else:
            return "Obesità estrema"

    def calcola_bfm(self):
        try:
            altezza_cm = self.user.profile.altezza
            sesso = self.user.profile.sesso
            if not altezza_cm or not sesso:
                return None

            if sesso == 'M':
                return round(
                    495 / (1.0324 - 0.19077 * math.log10(self.vita_cm - self.collo_cm) + 0.15456 * math.log10(altezza_cm)) - 450,
                    2
                )
            elif sesso == 'F' and self.fianchi_cm:
                return round(
                    495 / (1.29579 - 0.35004 * math.log10(self.vita_cm + self.fianchi_cm - self.collo_cm) + 0.22100 * math.log10(altezza_cm)) - 450,
                    2
                )
        except (ValueError, ZeroDivisionError):
            return None

    def save(self, *args, **kwargs):
        bmi = self.calcola_bmi
        self.bmi_valore = round(bmi, 2) if bmi is not None else None
        self.bmi_descr = self.calcola_descrizione_bmi(bmi)
        self.bfm = self.calcola_bfm()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.data}"

    class Meta:
        verbose_name_plural = "Misurazioni"
