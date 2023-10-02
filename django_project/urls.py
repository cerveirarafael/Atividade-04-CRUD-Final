"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appdoRafael import views

urlpatterns = [
    path('', views.meuSite),
    path('admin/', admin.site.urls),
    path('razao/', views.create_razao),
    path('razao/delete/<id>', views.delete_razao),
    path('razao/update/<id>', views.update_razao),
    path('tabela/', views.create_tabela),
    path('tabela/delete/<id>', views.delete_jogador),
    path('tabela/update/<id>', views.update_jogador),
    path('users/login/', views.login_user, name="login"),
    path('users/logout/', views.logout_user, name="logout"),
    path('users', views.create_user),
]
