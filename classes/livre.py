from classes.document import Document

class Livre (Document) :

    def __init__(self, titre, auteur, theme):
        super().__init__(titre, auteur, theme, type = "livre")

    def emprunter(self):
        self.est_disponible = False
        print("Nouveau statut du livre : Indisponible(Le livre a ete emprunte)")
    
    def retourner(self):
        self.est_disponible = True
        print("Le livre est a nouveau disponible")

    