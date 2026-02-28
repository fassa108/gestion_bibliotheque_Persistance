from classes.bibliothecaire import Bibliothcaire
import bcrypt

class Authentification :
    def __init__(self):
        pass

    @staticmethod
    def s_inscrire(user) :
        sql = """INSERT INTO bibliothecaire (nom, email, password) 
        VALUES (%s,%s,%s)"""
        parametre = (user.nom, user.email, user.password)
        succes = Bibliothcaire.executer_requete(sql, parametre)
        if succes :
            print("Admin ajoute")

    @staticmethod
    def se_connecter(email, password) :
        sql = """SELECT * FROM bibliothecaire WHERE email = %s"""
        resultat = Bibliothcaire.executer_requete(sql,(email,))

        if resultat != None :
            for ligne in resultat:
                if ligne['email'] == email and bcrypt.checkpw(password,ligne['password'].encode('utf-8')):
                        return ligne
                else :
                    print("Erreur!!!")
        return None