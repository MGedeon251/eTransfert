#controller de user

import os
import sys
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from database.connect import Database
from model.user import User

db = Database.connect_dbs()

class UserController() : 
    def __init__(self,login):
        self.user = User(db)
        self.login = login
    def login(self,user,password, UI_Principal,LogIn):
        if user and password:
            user = self.user.getUser(user,password)
            if user : 
                LogIn.hide()
                self.login.Form = QtWidgets.QMainWindow()
                self.login.ui = UI_Principal()
                self.login.ui.setupUi(self.login.Form)
                self.login.Form.show()
                print('Utilisateur connecté')
            else :
                print('Utilisateur non reconnu')