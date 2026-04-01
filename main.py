


class Utilisateur:
    def __init__(self, name, id):
        self.name = name
        self.id = id



    def peut_valider(self, competence_id: int) -> bool:
        return False


class Apprenant(Utilisateur):
    # Constructeur
    def __init__(self, name, id, competences_validees):
        super().__init__(name, id)
        self.competences_validees = competences_validees

    def peut_valider(self, competence_id: int) -> bool:
        if competence_id in self.competences_validees:
            return True
        else:
            return False


class Formateur(Utilisateur):
    def peut_valider(self, competence_id: int) -> bool:
        return True


if __name__ == "__main__":
    apprenant_1 = Apprenant("Bidule", 1, 1)
    print(apprenant_1.name)
    print(apprenant_1.id)
