from classes.bibliothecaire import Bibliothcaire
from classes.livre import Livre
from classes.magazine import Magazine
from classes.adherant import Adherant
from classes.auth_user import UserAuth
from classes.authentification import Authentification
import bcrypt


class Menu:
    def __init__(self):
        
        self.biblio = Bibliothcaire()
        self.auth = Authentification()

    
    def menu_connexion(self) :
        while True:
            print("1. Se Connecter")
            print("2. S'inscrire en tant qu'admin")
            print("0. Quitter")
            choix = input("Votre choix : ")
            match choix:
                case '1' :

                    email = self.biblio.demander_chaine("Email : ")
                    password = self.biblio.demander_mdp("Mot de passe : ")
                    password = password.encode('utf-8')
                    # password = bcrypt.hashpw(password, bcrypt.gensalt())
                    admin = self.auth.se_connecter(email, password)
                    if admin != None :
                        self.lancer_menu(admin)
                    else :
                        print("Email ou mot de passe incorrect!!!")
                case '2' :
                    nom = self.biblio.demander_chaine("Nom : ")
                    email = self.biblio.demander_chaine("Email : ")
                    password = self.biblio.demander_mdp("Mot de passe : ")
                    password = password.encode('utf-8')
                    password = bcrypt.hashpw(password, bcrypt.gensalt())
                    auth = UserAuth(nom, email, password)
                    Authentification.s_inscrire(auth)

                case '0' :
                    print("Bye!")
                    exit()

                case _: 
                    print("Choix invalide")



    def lancer_menu(self,admin) :
        print(f"Bienvenue {admin['nom']}")
        while True :
            print('~'*20 ,'GESTION DE BIBLIOTHEQUE', '~'*20 )
            print("1. Ajouter un document")
            print("2. Ajouter un Membre")
            print("3. Valider un emprunt")
            print("4. Retourner un document")
            print("5. Afficher les documents")
            print("6. Afficher les adherants")
            print("7. Afficher liste des emprunts")
            print("8. Rechercher un document")
            print("9. Quitter")
            choice = input("Choisir........: ")

            match choice :

                case '1' :
                    titre = Bibliothcaire.demander_chaine("Veuillez saisir le titre du livre: ")
                    auteur = Bibliothcaire.demander_chaine("Veuillez saisir l'auteur: ")
                    theme = Bibliothcaire.demander_chaine("Veuillez saisir le theme: ")

                    while True:
                        type_doc = input(
                            "Veuillez saisir le type de document (Livre ou Magazine) :\n" \
                            "1. magazine\n" \
                            "2. livre \n" \
                            "\t :  "
                        ).strip()
                        if type_doc == "1":
                            document = Magazine(titre, auteur, theme)
                            break
                        elif type_doc == "2":
                            document = Livre(titre, auteur, theme)
                            break
                        else:
                            print("Type de document non reconnu")

                    self.biblio.ajouter_document(document)

                case '2' :
                    while True:
                        nom = Bibliothcaire.demander_chaine("Veillez entrer votre nom: ").strip()
                        if nom.isalpha():
                            break
                        else:
                            print("Veuillez entrer un nom valide")

                    while True:
                        prenom = Bibliothcaire.demander_chaine("Veillez entrer votre prenom: ").strip()
                        if nom.isalpha():
                            break
                        else:
                            print("Veuillez entrer un prenom valide")

                    adherant = Adherant(nom,prenom)
                    self.biblio.ajouter_adherant(adherant)

                case '3' :
                    self.biblio.enregistrer_emprunt()

                case '4' :
                    self.biblio.recuperer_emprunt()

                case '5' :
                    self.biblio.afficher_document()
                
                case '6' :
                    self.biblio.afficher_adherant()

                case '7' : 
                    self.biblio.afficher_emprunt()

                case '8' :
                    mot = input("Veuillez entrer le titre, l'auteur ou l'id du document : ")
                    self.biblio.rechercher_document(mot)

                case '9' : 
                    break

                case _ : 
                    print("Choix invalide")

    


main = Menu()
main.menu_connexion()





    
