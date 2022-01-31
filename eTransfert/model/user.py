# Implementation model utilisateur 
# Un utilisateur pour le login

class User():
    def __init__(self,connect) :
        self.connect = connect
        with self.connect.cursor() as cursor:
            sql= """ CREATE TABLE IF NOT EXISTS user
                     (username VARCHAR(25) NOT NULL,
                      password varchar(255) not null )"""
            cursor.execute(sql)
            self.connect.commit()
            
    def getUser(self, user, password):
        with self.connect.cursor() as cursor:
            sql = """ SELECT username FROM user 
                        WHERE username = %s AND password = %s """
            cursor.execute(sql,(user,password))
            resultat_req= cursor.fetchone()
            return resultat_req
                    
    