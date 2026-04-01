


class Utilisateur:
    # Constructeur
    def __init__(self, name, id):
        self.name = name
        self.id = id



    def peut_valider(self, competence_id: int) -> bool:
        return False


class Apprenant(Utilisateur):
    # Constructeur
    def __init__(self, name, id, competences_validees):
        super().__init__(name, id)
        self._competences_validees = competences_validees

    def peut_valider(self, competence_id: int) -> bool:
        if competence_id in self._competences_validees:
            return True
        else:
            return False

    def ajouter_competence(self, competence_id: int):
        if competence_id in self._competences_validees:
            raise ValueError("La compétence exist déjà")
        else:
            self._competences_validees.append(competence_id)



class Formateur(Utilisateur):

    def peut_valider(self, competence_id: int) -> bool:
        return True



if __name__ == "__main__":
    apprenant_1 = Apprenant("Bidule", 1, [1,2,3])
    print(apprenant_1.name , apprenant_1.id, apprenant_1.peut_valider(1))
    apprenant_1.ajouter_competence(4)
    apprenant_1.ajouter_competence(1)



