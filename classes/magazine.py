from classes.document import Document

class Magazine(Document) :

    def __init__(self, titre, auteur, theme):
        super().__init__(titre, auteur, theme, type = 'magazine')
    
    def emprunter(self):
        self.est_disponible = False
        print("Nouveau statut du magazine : Indisponible(Le magazine a ete emprunte)")
    
    
    def retourner(self):
        self.est_disponible = True
        print("Le magazine est a nouveau disponible")
