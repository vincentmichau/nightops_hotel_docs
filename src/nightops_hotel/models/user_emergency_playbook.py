class UserEmergencyPlaybook:
    """Procédures utilisateur stabilisées pour mode secours."""
    PLAYBOOK = {
        'xml': ['Vérifier le fichier XML', 'Relancer import', 'Utiliser dernier état local', 'Exporter logs QA'],
        'template': ['Utiliser template exemple', 'Désactiver calcul suspect', 'Prévisualiser', 'Générer PDF secours'],
        'pdf': ['Réessayer PDF', 'Exporter HTML', 'Ouvrir PDF fallback', 'Imprimer via Windows'],
        'excel': ['Fermer Excel', 'Réessayer export', 'Exporter CSV secours'],
        'print': ['Ouvrir PDF', 'Changer imprimante', 'Imprimer manuellement', 'Informer réception'],
    }
    def steps(self, area):
        return list(self.PLAYBOOK.get(area, ['Réessayer', 'Exporter logs QA', 'Contacter support']))
    def validate(self):
        return {'ok': all(self.PLAYBOOK.values()), 'areas': list(self.PLAYBOOK.keys())}
