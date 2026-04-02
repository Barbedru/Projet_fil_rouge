import pytest

from utilisateurs.Apprenant import Apprenant
from utilisateurs.Formateur import Formateur
from utilisateurs.promotion import Promotion
from utilisateurs.Utilisateur import Utilisateur


def test_peut_valider() -> None:
    a = Apprenant("JéJé", 1, [1, 3, 7])
    assert a.peut_valider(1) == True
    assert a.peut_valider(99) == False

def test_ajouter_competence() -> None:
    a = Apprenant("JuJu", 3, [1])
    a.ajouter_competence(2)
    assert 2 in a._competences_validees

def test_ajouter_competence_doublon() -> None:
    a = Apprenant("ChaCha", 5, [1])
    with pytest.raises(ValueError):
        a.ajouter_competence(1)

def test_utilisateur_peut_valider() -> None:
    u = Utilisateur("TyTy", 1)
    assert u.peut_valider(1) == False

def test_formateur_peut_valider() -> None:
    f = Formateur("Bob", 2)
    assert f.peut_valider(1) == True
    assert f.peut_valider(99) == True

def test_promotion_ajouter_utilisateur() -> None:
    p = Promotion()
    u = Utilisateur("Alice", 1)
    p.ajouter_utilisateur(u)
    assert u in p.utilisateurs

def test_promotion_doublon() -> None:
    p = Promotion()
    u = Utilisateur("Alice", 1)
    p.ajouter_utilisateur(u)
    with pytest.raises(ValueError):
        p.ajouter_utilisateur(u)

#def test_promotion_fusion() -> None:
#    p1, p2 = Promotion(), Promotion()
#    u1, u2 = Utilisateur("Alice", 1), Utilisateur("Bob", 2)
#    p1.ajouter_utilisateur(u1)
#    p2.ajouter_utilisateur(u2)
#    p3 = p1 + p2
#    assert len(p3.utilisateurs) == 2