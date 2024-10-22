from django.urls import path
from . import views

# Définit les URL de l'application Toto
urlpatterns = [
    path('', views.record_list, name='record_list'),  # Page d'accueil avec la liste des enregistrements
    path('record/<int:pk>/', views.record_detail, name='record_detail'),  # Détails d'un enregistrement
    path('record/new/', views.record_create, name='record_create'),  # Création d'un nouvel enregistrement
    path('record/<int:pk>/edit/', views.record_update, name='record_update'),  # Modification d'un enregistrement
    path('record/<int:pk>/delete/', views.record_delete, name='record_delete'),  # Suppression d'un enregistrement
]