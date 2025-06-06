# Generated by Django 5.2.1 on 2025-05-19 09:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Allenamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('giorno', models.CharField(choices=[('giorno1', 'Giorno 1'), ('giorno2', 'Giorno 2'), ('giorno3', 'Giorno 3'), ('giorno4', 'Giorno 4')], max_length=10)),
                ('esercizio', models.CharField(blank=True, max_length=20, null=True)),
                ('serie', models.PositiveIntegerField()),
                ('ripetizioni', models.PositiveIntegerField()),
                ('peso', models.DecimalField(decimal_places=2, help_text='Peso in kg', max_digits=5)),
                ('note', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Allenamenti',
            },
        ),
        migrations.CreateModel(
            name='BenessereGiornaliero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(unique=True)),
                ('acqua_litri', models.DecimalField(decimal_places=2, help_text='Litri di acqua bevuti', max_digits=4)),
                ('sigarette_fumate', models.PositiveIntegerField(default=0, help_text='Numero di sigarette fumate')),
                ('note', models.TextField(blank=True, help_text='Note personali')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Benessere Giornaliero',
            },
        ),
        migrations.CreateModel(
            name='DiarioAlimentare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('tipologia_pasto', models.CharField(choices=[('colazione', 'Colazione'), ('spuntino_mattina', 'Spuntino Mattina'), ('pranzo', 'Pranzo'), ('spuntino_pomeriggio', 'Spuntino Pomeriggio'), ('cena', 'Cena'), ('spuntino_sera', 'Spuntino Sera')], max_length=20)),
                ('descrizione', models.TextField(help_text='Cosa hai mangiato?')),
                ('calorie', models.PositiveIntegerField(blank=True, help_text='Calorie (facoltativo)', null=True)),
                ('note', models.TextField(blank=True, help_text='Note aggiuntive (facoltative)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Diario Alimentare',
            },
        ),
        migrations.CreateModel(
            name='Misurazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('sesso', models.CharField(choices=[('M', 'Maschio'), ('F', 'Femmina')], max_length=1)),
                ('altezza_cm', models.PositiveIntegerField(help_text='In cm')),
                ('peso_kg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vita_cm', models.PositiveIntegerField(help_text='Circonferenza vita (cm)')),
                ('collo_cm', models.PositiveIntegerField(help_text='Circonferenza collo (cm)')),
                ('fianchi_cm', models.PositiveIntegerField(blank=True, help_text='Solo per donne (cm)', null=True)),
                ('note', models.TextField(blank=True)),
                ('bmi_valore', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bmi_descr', models.CharField(blank=True, max_length=20, null=True)),
                ('bfm', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Misurazioni',
            },
        ),
    ]
