from django.db import models

# Modèle représentant un enregistrement dans l'application
class Record(models.Model):
    title = models.CharField(max_length=100)  # Titre de l'enregistrement
    description = models.TextField()           # Description de l'enregistrement
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)      # Date de mise à jour

    def __str__(self):
        return self.title  # Retourne le titre de l'enregistrement pour l'affichage