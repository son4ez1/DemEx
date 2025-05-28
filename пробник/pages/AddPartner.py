from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidget, QMessageBox,QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox
)
import sqlite3

import re
from pages.SavePartner import SavePartner


class AddPartner(QDialog):
    def __init__(self, ui, cursor):
        super(AddPartner, self).__init__()
        self.ui = ui
        self.cursor = cursor # 17 шаг: добавляем строчки с 1 по 15
        self.SavePartner = SavePartner(ui, cursor, inn=None)  # 24 шаг: добавляем строчки 16 и 19

        self.SavePartner.clear_inputs()
        self.SavePartner.load_types()

        self.Add_but = self.ui.findChild(QPushButton, "Add_button") # 29 шаг: добавляем строчки с 21 по 22 (запускаем)
        self.Add_but.clicked.connect(self.SavePartner.save_partner)