


class Utilisateur:
    # Constructeur
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"{self.name} - {self.id}"


    def peut_valider(self, competence_id: int) -> bool:
        return False

class Promotion:
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

    ####Test ajout compétences
    #apprenant_1 = Apprenant("Bidule", 1, [1,2,3])
    #print(apprenant_1.name , apprenant_1.id, apprenant_1.peut_valider(1))
    #apprenant_1.ajouter_competence(4)

    ####Test ajout utilisateru à promotion
    #promotion_1 = Promotion()
    #utilisateur_1 = Utilisateur("Truc",2)

    #promotion_1.ajouter_utilisateur(utilisateur_1)
    #promotion_1.ajouter_utilisateur(utilisateur_1)

    #print(apprenant_1)

    ####Test fusion de Promotion

    p1 = Promotion()
    p2 = Promotion()

    p1.ajouter_utilisateur(Utilisateur("Machin", 1))
    p2.ajouter_utilisateur(Utilisateur("Bidule",2))
    p3 = p1 + p2

    for utilisateur in p3.utilisateurs:
        print(utilisateur)



