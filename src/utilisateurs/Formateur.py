from utilisateurs.Utilisateur import Utilisateur


class Formateur(Utilisateur):

    def peut_valider(self, competence_id: int) -> bool:
        return True
