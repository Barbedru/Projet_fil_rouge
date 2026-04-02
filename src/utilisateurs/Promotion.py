
from utilisateurs.Utilisateur import Utilisateur


class Promotion:
    # Initialise une liste vide d’utilisateurs
    def __init__(self):
        self.utilisateurs = []

    def ajouter_utilisateur(self, utilisateur: Utilisateur):
        if utilisateur in self.utilisateurs:
            raise ValueError("L'utilisateur déjà existe déjà")
        else:
            self.utilisateurs.append(utilisateur)

    def __add__(self, other):
        p3 = Promotion()
        for utilisateur in self.utilisateurs:
            p3.ajouter_utilisateur(utilisateur)
        for utilisateur in other.utilisateurs:
            p3.ajouter_utilisateur(utilisateur)
        return p3