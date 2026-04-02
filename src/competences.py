from dataclasses import dataclass, field


@dataclass
class Apprenant:
    nom: str
    promo: str
    competences: list[]


def creer_apprenant(nom : str , promo : str) -> Apprenant:
    return {"nom": nom, "promo": promo, "competences": []}

def valider_competence(apprenant, competence):
    if competence not in apprenant["competences"]:
        apprenant["competences"].append(competence)

def peut_valider(apprenant : str, competence):
    return competence in apprenant["competences"]

def afficher_progression(apprenants):
    for a in apprenants:
        nb = len(a["competences"])
        print(f"{a['nom']} : {nb} compétence(s) validée(s)")

def trouver_par_nom(apprenants, nom):
    for a in apprenants:
        if a["nom"] == nom:
            return a
    return None

def statistiques(apprenants):
    total = 0
    for a in apprenants:
        total += len(a["competences"])
    if len(apprenants) == 0:
        return 0
    return total / len(apprenants)

