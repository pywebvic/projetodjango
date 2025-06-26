from django.urls import path
from . import views # <-- Importa as views do arquivo views.py desta aplicação

urlpatterns = [
    path('login/', views.login), # Mapeia a URL raiz desta aplicação ('' ) para a função home_view
    path('', views.home_view, name='home'), # Mapeia a URL raiz desta aplicação ('' ) para a função home_view
]
