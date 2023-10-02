from django.shortcuts import render, redirect
from .models import Razoes, Edicao, Tabela
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


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

@login_required
def create_razao(request):
    if request.method == "POST":
        Razoes.objects.create(
            titulo=request.POST["titulo"],
            razao=request.POST["razao"],
            importancia=request.POST["importancia"],
            dataDeCadaAngustia=request.POST["dataDeCadaAngustia"])

        return redirect(meuSite)
    return render(request, "formRazao.html", context={"action": "Adicionar"})

@login_required
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

@login_required
def delete_razao(request, id):
  razao = Razoes.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      razao.delete()

    return redirect(meuSite)
  return render(request, "are_you_sure.html", context={"razao": razao})

@login_required
def create_tabela(request):
    if request.method == "POST":
        Tabela.objects.create(
            jogador=request.POST["jogador"],
            jogos=request.POST["jogos"],
            gols=request.POST["gols"])
        return redirect(meuSite)
    return render(request, "form.html", context={"action": "Adicionar"})

@login_required
def delete_jogador(request, id):
  jogador = Tabela.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      jogador.delete()

    return redirect(meuSite)
  return render(request, "are_you_sure.html", context={"tabela": jogador})

@login_required
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

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect(meuSite)
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect(meuSite)
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect(meuSite)