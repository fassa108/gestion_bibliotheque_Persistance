from abc import ABC, abstractmethod

class Document :
    def __init__(self,titre,auteur,theme,type):
        self.id = None
        self.titre = titre
        self.auteur = auteur
        self.theme = theme
        self.type = type
        self.__disponibilite = True
    

    @property
    def est_disponible(self):
        return self.__disponibilite
    
    @est_disponible.setter
    def est_disponible(self,valeur):
        if not isinstance(valeur,bool) :
            raise ("La valeur doit etre un booleen")
        else :
            self.__disponibilite = valeur

    def __str__(self):
        return f"--> ID : {self.id} | TYPE : {self.type} | TITRE : {self.titre} | AUTEUR : {self.auteur} | THEME : {self.theme}"
    

    @abstractmethod
    def emprunter(self) :
        pass

    @abstractmethod
    def retourner(self):
        pass