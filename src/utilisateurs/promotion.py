
from utilisateurs.Utilisateur import Utilisateur


class Promotion:
    # Initialise une liste vide d’utilisateurs
    def __init__(self) -> None:
        self.utilisateurs: list[Utilisateur] = []

    def ajouter_utilisateur(self, utilisateur: Utilisateur) -> None:
        if utilisateur in self.utilisateurs:
            raise ValueError("L'utilisateur déjà existe déjà")
        else:
            self.utilisateurs.append(utilisateur)

   # def __add__(self, promotion: "Promotion") -> "Promotion":
