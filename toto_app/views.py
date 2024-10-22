from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from .forms import RecordForm  # Importe le formulaire pour les enregistrements

# Affiche la liste des enregistrements
def record_list(request):
    records = Record.objects.all()  # Récupère tous les enregistrements
    return render(request, 'list.html', {'records': records})

# Affiche les détails d'un enregistrement
def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)  # Récupère l'enregistrement par son ID
    return render(request, 'detail.html', {'record': record})

# Crée un nouvel enregistrement
def record_create(request):
    if request.method == "POST":
        form = RecordForm(request.POST)  # Crée un formulaire avec les données POST
        if form.is_valid():  # Vérifie la validité du formulaire
            form.save()  # Enregistre le nouvel enregistrement
            return redirect('record_list')  # Redirige vers la liste des enregistrements
    else:
        form = RecordForm()  # Crée un formulaire vide
    return render(request, 'create.html', {'form': form})

# Met à jour un enregistrement existant
def record_update(request, pk):
    record = get_object_or_404(Record, pk=pk)  # Récupère l'enregistrement par son ID
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)  # Crée un formulaire avec les données POST et l'instance de l'enregistrement
        if form.is_valid():  # Vérifie la validité du formulaire
            form.save()  # Enregistre les modifications
            return redirect('record_detail', pk=record.pk)  # Redirige vers les détails de l'enregistrement mis à jour
    else:
        form = RecordForm(instance=record)  # Pré-remplit le formulaire avec les données de l'enregistrement

    # Assurez-vous que la fonction retourne toujours un HttpResponse
        return render(request, 'update.html', {'form': form, 'record': record})

# Supprime un enregistrement
def record_delete(request, pk):
    record = get_object_or_404(Record, pk=pk)  # Récupère l'enregistrement par son ID
    if request.method == "POST":
        record.delete()  # Supprime l'enregistrement
        return redirect('record_list')  # Redirige vers la liste des enregistrements
    return render(request, 'delete.html', {'record': record})  # Affiche une page de confirmation de suppression