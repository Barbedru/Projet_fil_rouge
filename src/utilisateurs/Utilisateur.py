class Utilisateur:
    # Constructeur
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    # équivalent toString - permet d'afficher un utilisateur proprement
    def __str__(self) -> str:
        return f"{self.name} - {self.id}"

    # méthode pouvant être utilisé dans les classes enfants
    def peut_valider(self, competence_id: int) -> bool:
        return False