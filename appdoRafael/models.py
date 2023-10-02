from django.db import models

# Create your models here.
class Razoes(models.Model):
  titulo = models.CharField(max_length=50)
  razao = models.CharField(max_length=600)
  importancia = models.CharField(max_length=50)
  dataDeCadaAngustia = models.CharField(max_length=50)

class Edicao(models.Model):
  NOTA = [
    ("Campeão","10"),
    ("Vice","5"),
    ("Semifinalista","4"),
    ("Quartas","3"),
    ("Oitavas","2"),
    ("Fase de Grupos","1"),
    ("Pré-Libertadores","0"),
  ]
  
  rankEdicao = rankEdicao = models.CharField(max_length=10)
  anoEdicao = models.CharField(max_length=30)
  desempenho = models.CharField(max_length=20)
  qualidadeDesempenho = models.CharField(max_length = 20, choices = NOTA)

class Tabela(models.Model):
  jogador = models.CharField(max_length=50)
  jogos = models.CharField(max_length=3)
  gols = models.CharField(max_length=4)

