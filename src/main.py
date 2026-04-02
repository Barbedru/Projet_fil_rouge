from dataclasses import dataclass



@dataclass
class Competence:
    id : int
    nom : str

competences = [
    Competence(1,"Python"),
    Competence(2,"JavaScript"),
    Competence(3,"Html"),
    Competence(4,"Java"),
    Competence(5,"PHP"),
    Competence(6,"C#"),
    Competence(7,"SQL"),
    Competence(8,"Laravel"),
    Competence(9,"JavaScript"),
    Competence(10,"Css"),
]


@dataclass
class Validation:
    id : int
    apprenant_id : int
    competence_id : int
    statut : str
    pre_valid_par : bool





if __name__ == "__main__":
   print(competences)






