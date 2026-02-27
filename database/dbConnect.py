import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


class DbConnect :
    def __init__(self):
        self.db_config = {
            'host' : os.getenv("DB_HOST"),
            'user' : os.getenv("DB_USER"),
            'password' : os.getenv("DB_PASS"),
            'database' : os.getenv("DB_NAME")
        }
        self.connexion = None

    def __enter__(self) :
        try :
            self.connexion = mysql.connector.connect(**self.db_config)
            # print("Connexion etablie")
            return self.connexion
        except mysql.connector.Error as error :
            print(f"Echec de la connexion : {error}")
            return None

    def __exit__(self, exc_type, exc_val, exc_tb) :
        if self.connexion and self.connexion.is_connected() :
            self.connexion.close()
            # print("Connexion fernmee")

# conn = DbConnect()

# with DbConnect() as conn:
#     if conn :
#         with conn.cursor() as curseur :
#             print("J'ai reussi!!!")


    