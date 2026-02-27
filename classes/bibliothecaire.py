from classes.livre import Livre
from classes.magazine import Magazine
from classes.adherant import Adherant
from database.dbConnect import DbConnect

class Bibliothcaire() :
    def __init__(self):
        self.liste_adherants = []
        self.liste_documents = []


    def executer_requete(self,sql,parametre = None) :
        with DbConnect() as conn :
            if conn :
                with conn.cursor(dictionary=True) as curseur :
                    curseur.execute(sql,parametre or ())
                    if sql.strip().upper().startswith("SELECT") :
                        return curseur.fetchall()
                    else :
                        conn.commit()
                        return curseur.rowcount
            else :
                print("Erreur!!! L'operation a echoue verifier la connexion")

    def ajouter_document(self, document) :
        sql = """INSERT INTO documents (titre,auteur,theme,type)
                    VALUES (%s, %s, %s, %s)"""
        arguments = (document.titre, document.auteur, document.theme, document.type)
        succes = self.executer_requete(sql, arguments)
        if succes != 0 :
            print("Document ajoute avec succes!")
        else :
            print("Erreur lors de l'ajout")

    

    def ajouter_adherant(self, adherant) :
        sql = """INSERT INTO adherants (nom, prenom) VALUES (%s, %s)"""
        arguments = (adherant.nom, adherant.prenom)
        succes = self.executer_requete(sql, arguments)
        if succes != 0 :
            print("Adherant ajouter avec succes!")
        else: 
            print("Erreur lors de l'ajout")
        


    def afficher_adherant(self) :
        sql = """SELECT * FROM adherants"""
        resultats = self.executer_requete(sql)
        if resultats :
            for resultat in resultats :
                print(f"--> ID : {resultat['id']} | Prenom : {resultat['prenom']}  | Nom : {resultat['nom']}")
            return resultats


    def afficher_document(self) :
        sql = """SELECT * FROM documents"""
        resultats = self.executer_requete(sql)
        if resultats :
            for resultat in resultats :
                dispo = 'Disponible' if resultat['disponibilite'] else 'Non disponible'
                print(f"--> ID : {resultat['id']} | TYPE : {resultat['type']} | TITRE : {resultat['titre']} | AUTEUR : {resultat['auteur']} | THEME : {resultat['theme']} |::| {dispo}")
            return resultats
        else :
            print("Aucun document pour le moment")


    def recuperer_adherant(self) :
        liste_adherant = self.afficher_adherant()
        choix = input("Veuillez saisir l'ID de l'adherant : ")
        for adherant in liste_adherant :
            if str(adherant['id']) == choix :
                id_adherant = adherant['id']
                return id_adherant

        
        return None
        

    def recuperer_document(self) :
        liste_document = self.afficher_document()
        choix = input("Veuillez saisir l'ID du document : ")
        for document in liste_document :
            if str(document['id']) == choix and document['disponibilite'] == True:
                id_document = document['id']
                return id_document
            else :
                print("Livre indisponible ou ID invalide!")
        
        return None



    def enregistrer_emprunt(self) :
        id_adherant = self.recuperer_adherant()
        id_document = self.recuperer_document()

        if id_adherant and id_document :
            sql = """INSERT INTO emprunts (id_adherant, id_document) VALUES (%s, %s)"""
            arguments = (id_adherant, id_document)
            succes = self.executer_requete(sql, arguments)
            if succes :
                query = """UPDATE documents SET disponibilite = %s WHERE id = %s"""
                params = (False,id_document)
                self.executer_requete(query,params)
                print("Emprunt Enregistre")
            else :
                print("L'enregistrement de l'emprunt a echoue")



    def afficher_emprunt(self) :
        sql = """SELECT e.*,a.nom, a.prenom, d.titre   
        FROM emprunts e 
        JOIN adherants a ON e.id_adherant = a.id 
        JOIN documents d ON d.id = e.id_document"""
        resultats = self.executer_requete(sql)
        if resultats :
            for emprunt in resultats :
                
                print(f" Identifiant : {emprunt['id']} | Date : {emprunt['date_emprunt']} | titre document : {emprunt['titre']} | nom et prenom adherant : {emprunt['nom']} {emprunt['prenom']} | etat : {emprunt['etat']}")
            return resultats
        else:
            print("Aucun emorunt pour le moment!")
            return None

    def recuperer_emprunt(self) :
        liste = self.afficher_emprunt()
        choix = input("Veuillez saisir l' ID de l'emprunt que vous voulez marque retourne : ")
        
        for e in liste :
            if str(e['id']) == choix and e['etat'] == 'en cours' :
                return e
            
        return None

    def retourner_document(self) :
        emprunt = self.recuperer_emprunt()
        if emprunt == None :
            print("Le livre a deja ete rendu ou ID invalide!")
        else :
            id_emprunt = emprunt['id']
            sql = """UPDATE emprunts SET etat = %s WHERE id = %s"""
            arguments = ('retourne',id_emprunt)
            succes = self.executer_requete(sql,arguments)
            if succes :
                query = """UPDATE documents SET disponibilite = %s WHERE id = %s"""
                params = (True,id_emprunt)
                self.executer_requete(query,params)
                print("Emprunt modifier avec succes")
            else :
                print("Erreur lors de la modification!")



    def rechercher_document(self,mot) :
        if mot.isdigit() :
            mot = int(mot)
            sql = """SELECT * FROM documents WHERE id = %s"""
            argument = (mot,)
        else :
            mot_cle = f"%{mot}%"
            sql = """SELECT * FROM documents WHERE titre LIKE %s OR auteur LIKE %s"""
            argument = (mot_cle,mot_cle)
        resultats = self.executer_requete(sql,argument)
        if resultats == None :
            print("Aucun document trouve!")
        else :
            for resultat in resultats :
                dispo = 'Disponible' if resultat['disponibilite'] else 'Non disponible'
                print(f"--> ID : {resultat['id']} | TYPE : {resultat['type']} | TITRE : {resultat['titre']} | AUTEUR : {resultat['auteur']} | THEME : {resultat['theme']} |::| {dispo}")

