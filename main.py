from classes.bibliothecaire import Bibliothcaire
from classes.livre import Livre
from classes.magazine import Magazine
from classes.adherant import Adherant



class Menu:
    def __init__(self):
        self.biblio = Bibliothcaire()


    def lancer_menu(self) :
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
                    titre = input("Veuillez saisir le titre du livre: ")
                    auteur = input("Veuillez saisir l'auteur: ")
                    theme = input("Veuillez saisir le theme: ")

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
                        nom = input("Veillez entrer votre nom: ").strip()
                        if nom.isalpha():
                            break
                        else:
                            print("Veuillez entrer un nom valide")

                    while True:
                        prenom = input("Veillez entrer votre prenom: ").strip()
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
                    exit()

                case _ : 
                    print("Choix invalide")

                    


main = Menu()
main.lancer_menu()