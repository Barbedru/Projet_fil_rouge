from utilisateurs.Utilisateur import Utilisateur


# Class qui hérite d'Utilisateur
class Apprenant(Utilisateur):

    # Constructeur
    def __init__(self, name : str, id: int, competences_validees : list[int]) -> None:
        super().__init__(name, id)
        self._competences_validees = competences_validees

    def peut_valider(self, competence_id: int) -> bool:
        if competence_id in self._competences_validees:
            return True
        else:
            return False

    def ajouter_competence(self, competence_id: int) -> None:
        if competence_id in self._competences_validees:
            raise ValueError("La compétence exist déjà")
        else:
            self._competences_validees.append(competence_id)


apprenants = [
    Apprenant ("JéJé",1,[1,3,7]),
    Apprenant ("Anne-Laure",2,[1,2,3]),
    Apprenant ("JuJu",3,[1]),
    Apprenant ("CléClé",4,[1,2,3,6,7]),
    Apprenant ("ChaCha",5,[1]),
    Apprenant ("TyTy",6,[]),
]