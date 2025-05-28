from PyQt5 import QtWidgets # 34 шаг: добавляем строчки с 1 по 73 (удаляем строчки где есть SalesHistory)
from PyQt5.QtWidgets import (
    QDialog, QTableWidget, QMessageBox,QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox
)
import sqlite3
from pages.db import  get_partner_data
import re
from pages.SavePartner import SavePartner
from pages.SalesHistory import SalesHistory # 41 шаг: добавляем строчку 9



class EditPartner(QDialog):
    def __init__(self, ui, cursor, inn):
        super(EditPartner, self).__init__()
        self.ui = ui
        self.cursor = cursor
        self.inn = inn
        self.SavePartner = SavePartner(ui, cursor, inn)
    
        #поля ввода
        self.inn_input = self.ui.findChild(QLineEdit, "inn_input")
        self.name_input = self.ui.findChild(QLineEdit, "name_input")
        self.rating_spin = self.ui.findChild(QSpinBox, "rating_spin")
        self.index_input = self.ui.findChild(QLineEdit, "index_input")
        self.phone_input = self.ui.findChild(QLineEdit, "phone_input")
        self.email_input = self.ui.findChild(QLineEdit, "email_input")
        self.director_last_name_input = self.ui.findChild(QLineEdit, "director_last_name_input")
        self.director_first_name_input = self.ui.findChild(QLineEdit, "director_first_name_input")
        self.director_middle_name_input = self.ui.findChild(QLineEdit, "director_middle_name_input")
        self.region_input = self.ui.findChild(QLineEdit, "region_input")
        self.city_input = self.ui.findChild(QLineEdit, "city_input")
        self.street_input = self.ui.findChild(QLineEdit, "street_input")
        self.house_input = self.ui.findChild(QLineEdit, "house_input")
        
        self.type_combo = self.ui.findChild(QComboBox, "type_combo")
      
        #print("Выбранный тип (текст):", selected_text)        
        self.SavePartner.load_types()

        self.load_partner_data()

        self.btnSave = self.ui.findChild(QPushButton, "btnSave")
        self.btnSave.clicked.connect(self.SavePartner.save_partner)

        self.btnHistory = self.ui.findChild(QPushButton, "btnHistory")# 39 шаг: добавляем строчки с 46 по 47
        self.btnHistory.clicked.connect(self.next)


    def load_partner_data(self): #заполнение полей в соответсвии с инн, который бередтся в PartnersView с нажатия на партнера
 
        try:
            #inn = self.inn_input.text()
            partner = get_partner_data(self.cursor, self.inn)
            print(partner)
            if partner:
                self.inn = partner[0]
                self.inn_input.setText(str(partner[0]))
                self.name_input.setText(partner[1])
                self.type_combo.setCurrentIndex(partner[2] - 1)
                self.rating_spin.setValue(partner[3])
                self.phone_input.setText(partner[12])
                self.email_input.setText(partner[13])
                self.index_input.setText(str(partner[4]))
                self.region_input.setText(partner[5])
                self.city_input.setText(partner[6])
                self.street_input.setText(partner[7])
                self.house_input.setText(partner[8])
                self.director_last_name_input.setText(partner[9])
                self.director_first_name_input.setText(partner[10])
                self.director_middle_name_input.setText(partner[11])
        except Exception as e:
            print(f"Ошибка при загрузке данных партнера: {e}")

    def next(self): # 38 шаг: добавляем строчки с 75 по 77 
        self.ui.stackedWidget.setCurrentWidget(self.ui.SaleHistory) #SaleHistory страницас историей 
        self.lybaya = SalesHistory(self.ui, self.cursor, self.inn)

