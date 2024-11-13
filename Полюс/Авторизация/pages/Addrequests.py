from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, # это базовый класс диалогового окна
    QTableWidgetItem 
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

class Addrequests(QDialog):
    def __init__(self):        
        super(Addrequests, self).__init__()
        #self.saveButton.clicked.connect(self.save) 
        print("ok")
        
    def save(self):
        print("647")