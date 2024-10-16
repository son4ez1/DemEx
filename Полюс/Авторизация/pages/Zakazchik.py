from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

class Zakazchik(QDialog):
    def __init__(self):        
        super(Zakazchik, self).__init__()
        print("ok")