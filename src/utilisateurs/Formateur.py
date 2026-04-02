from utilisateurs.Utilisateur import Utilisateur


class Formateur(Utilisateur):

    def peut_valider(self, competence_id: int) -> bool:
        return True

formateurs = [
    Formateur ("f1",1),
    Formateur ("f2",2),
    Formateur ("f3",3),
    ]