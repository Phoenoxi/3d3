class Local():
    def __init__(self,numero : str,capacite : int):
        self.numero = numero
        self.capacite = capacite

    def type_local(self):
        return "Local"
    
    def __str__(self):
        return f"Local {self.numero} |  Capacite : {self.capacite} place"
  