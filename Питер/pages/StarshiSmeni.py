from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, 
    QTableWidgetItem# это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

class StarshiSmeni(QDialog):
    def __init__(self, tadle):        
        super(StarshiSmeni, self).__init__()
        print("ok")
        self.tableWidget_StarshiSmeni = tadle
        print(tadle)
        self.vivod()