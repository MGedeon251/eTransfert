#module de connexion à la base de donnée
import mysql.connector
from mysql.connector import errorcode

class Database:
    #Cette classe est utimlisé pour l'initialisation de la connection avec une base de donnée MYSQL 
    @staticmethod
    def connect_dbs():
        try:
            cnn = mysql.connector.connect(
                user='root',
                password='',
                host='localhost',
                database='etransfertdb'  )
            # Si la connexion aboutie alors affiche ce message
            print("\nSYSTEM MESSAGE : MYSQL DATABASE CONNECTED\n") #
            return cnn
            
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Qu'elle que chose ne s'est pas bien passe ")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de donnée n'existe pas ")
            else:
                print(e)
    



