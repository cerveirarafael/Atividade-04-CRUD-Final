# Generated by Django 3.2.13 on 2023-09-14 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdoRafael', '0002_alter_edicao_qualidadedesempenho'),
    ]

    operations = [
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
