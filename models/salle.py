from models.local import Local

class Salle(Local):
    
    def __init__(self, numero: str, capacite: int):
        super().__init__(numero, capacite)

    def type_salle(self):
        return "Salle de cours"

    def __str__(self):
        return f"Local {self.numero} |  Capacite : {self.capacite} place | Salle de cours"
    
