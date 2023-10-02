from django.shortcuts import render, redirect
from .models import Razoes, Edicao, Tabela


# Create your views here.
def meuSite(request):
    razao = Razoes.objects.all()
    edicao = Edicao.objects.all()
    tabela = Tabela.objects.all()
    return render(request,
                  "meuSite.html",
                  context={
                      'razao': razao,
                      'edicao': edicao,
                      'tabela': tabela
                  })


def create_razao(request):
    if request.method == "POST":
        Razoes.objects.create(
            titulo=request.POST["titulo"],
            razao=request.POST["razao"],
            importancia=request.POST["importancia"],
            dataDeCadaAngustia=request.POST["dataDeCadaAngustia"])

        return redirect(meuSite)
    return render(request, "formRazao.html", context={"action": "Adicionar"})

def update_razao(request, id):
  razao = Razoes.objects.get(id = id)
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    razao.titulo = request.POST["titulo"]
    razao.razao = request.POST["razao"]
    razao.importancia = request.POST["importancia"]
    razao.dataDeCadaAngustia = request.POST["dataDeCadaAngustia"]
    razao.save()

    return redirect(meuSite)
  return render(request, "formRazao.html", context={"action": "Atualizar","razao": razao})

def delete_razao(request, id):
  razao = Razoes.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      razao.delete()

    return redirect(meuSite)
  return render(request, "are_you_sure.html", context={"razao": razao})

def create_tabela(request):
    if request.method == "POST":
        Tabela.objects.create(
            jogador=request.POST["jogador"],
            jogos=request.POST["jogos"],
            gols=request.POST["gols"])
        return redirect(meuSite)
    return render(request, "form.html", context={"action": "Adicionar"})

def delete_jogador(request, id):
  jogador = Tabela.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      jogador.delete()

    return redirect(meuSite)
  return render(request, "are_you_sure.html", context={"tabela": jogador})

def update_jogador(request, id):
  jogador = Tabela.objects.get(id = id)
  if request.method == "POST":
    # criar um novo filme usando os valors do meu formulário
    jogador.jogador = request.POST["jogador"]
    jogador.jogos = request.POST["jogos"]
    jogador.gols = request.POST["gols"]
    jogador.save()

    return redirect(meuSite)
  return render(request, "form.html", context={"action": "Atualizar","jogador": jogador})