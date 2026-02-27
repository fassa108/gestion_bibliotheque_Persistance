class Adherant :
    def __init__(self, nom, prenom):
        self.id = None
        self.nom = nom
        self.prenom = prenom


    def __str__(self):
        return f"ID : {self.id} | NOM : {self.nom} | PRENOM {self.prenom}"
    

    
        