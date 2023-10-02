# Generated by Django 3.2.13 on 2023-10-02 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rankEdicao', models.CharField(max_length=10)),
                ('anoEdicao', models.CharField(max_length=30)),
                ('desempenho', models.CharField(max_length=20)),
                ('qualidadeDesempenho', models.CharField(choices=[('Campeão', '10'), ('Vice', '5'), ('Semifinalista', '4'), ('Quartas', '3'), ('Oitavas', '2'), ('Fase de Grupos', '1'), ('Pré-Libertadores', '0')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Razoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('razao', models.CharField(max_length=600)),
                ('importancia', models.CharField(max_length=50)),
                ('dataDeCadaAngustia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jogador', models.CharField(max_length=50)),
                ('jogos', models.CharField(max_length=3)),
                ('gols', models.CharField(max_length=4)),
            ],
        ),
    ]
