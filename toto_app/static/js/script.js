// script.js

document.addEventListener('DOMContentLoaded', function() {
    // Affiche un message d'alerte lors de la tentative de suppression
    const deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const confirmation = confirm("Êtes-vous sûr de vouloir supprimer cet enregistrement ?");
            if (!confirmation) {
                event.preventDefault(); // Empêche la suppression si l'utilisateur annule
            }
        });
    });
});