from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidget, QMessageBox,QLabel, QPushButton, QLineEdit, QComboBox, QSpinBox
)
import sqlite3
from pages.db import get_partner_types, add_partner, update_partner # 23 шаг: добавляем строчку 6 (пока только функцию get_partner_types) # 28 шаг: добавляем add_partner, update_partner
import re


class SavePartner(QDialog):
    def __init__(self, ui, cursor, inn):
        super(SavePartner, self).__init__()
        self.ui = ui
        self.cursor = cursor
        self.inn = inn # 16 шаг: добавляем строчки с 1 по 15


        # поля в форме менять названия
        self.inn_input = self.ui.findChild(QLineEdit, "inn_input")# 20 шаг: добавляем строчки с 19 по 62
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
        selected_text = self.type_combo.currentText()
        #print("Выбранный тип (текст):", selected_text)        
        #self.load_types()

        #поля ошибок   
        #поля ошибок в форме менять названия    
        self.inn_error = self.ui.findChild(QLabel, "inn_error")
        self.name_error = self.ui.findChild(QLabel, "name_error")
        self.rating_error = self.ui.findChild(QLabel, "rating_error")
        self.index_error = self.ui.findChild(QLabel, "index_error")
        self.director_error = self.ui.findChild(QLabel, "director_error")
        self.phone_error = self.ui.findChild(QLabel, "phone_error")
        self.email_error = self.ui.findChild(QLabel, "email_error")

    def clear_inputs(self):
        self.inn_input.clear()
        self.name_input.clear()
        self.rating_spin.setValue(0)
        self.index_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.director_last_name_input.clear()
        self.director_first_name_input.clear()
        self.director_middle_name_input.clear()
        self.region_input.clear()
        self.city_input.clear()
        self.street_input.clear()
        self.house_input.clear()
        self.type_combo.setCurrentIndex(0)


    def load_types(self): # 21 шаг: добавляем строчки с 65 по 72
        self.type_combo.clear()
        try:
            types = get_partner_types(self.cursor) #get_partner_types функция в файле db 
            for type_id, type_name in types:
                self.type_combo.addItem(type_name, type_id)
        except Exception as e:
            print(f"Ошибка при загрузке типов партнеров: {e}")

    def validate_input(self): # 26 шаг: добавляем строчки с 74 по 199
        valid = True
        
        inn = self.inn_input.text() #inn - название сами задаете inn_input - поле ввода инн из формы
        print(inn)
        if not inn.isdigit() or len(inn) != 12: #inn
            self.inn_error.setText("ИНН должен содержать ровно 12 цифр") #self.inn_error - поле ошибки
            self.inn_error.show() #self.inn_error - поле ошибки
            valid = False
        else:
            self.inn_error.hide()

        name = self.name_input.text().strip()
        if not name:
            self.name_error.setText("Наименование не может быть пустым")
            self.name_error.show()
            valid = False
        else:
            self.name_error.hide()

        rating = self.rating_spin.value()
        if not (0 <= rating <= 10):
            self.rating_error.setText("Рейтинг должен быть от 0 до 10")
            self.rating_error.show()
            valid = False
        else:
            self.rating_error.hide()

        index = self.index_input.text()
        if not index.isdigit() or len(index) != 6:
            self.index_error.setText("Индекс должен содержать 6 цифр")
            self.index_error.show()
            valid = False
        else:
            self.index_error.hide()

        phone = self.phone_input.text()
        if not re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', phone):
            self.phone_error.setText("Формат: +7 XXX XXX XX XX")
            self.phone_error.show()
            valid = False
        else:
            self.phone_error.hide()

        email = self.email_input.text()
        if not re.match(r'.+@.+\..+', email):
            self.email_error.setText("Неверный формат email")
            self.email_error.show()
            valid = False
        else:
            self.email_error.hide()

        director_fields = [
            self.director_last_name_input.text().strip(),
            self.director_first_name_input.text().strip(),
            self.director_middle_name_input.text().strip()
        ]
        if not all(director_fields):
            self.director_error.setText("Заполните ФИО директора полностью")
            self.director_error.show()
            valid = False
        else:
            self.director_error.hide()

        return valid
    
    def clear_inputs(self):
        self.inn_input.clear()
        self.name_input.clear()
        self.rating_spin.setValue(0)
        self.index_input.clear()
        self.phone_input.clear()
        self.email_input.clear()
        self.director_last_name_input.clear()
        self.director_first_name_input.clear()
        self.director_middle_name_input.clear()
        self.region_input.clear()
        self.city_input.clear()
        self.street_input.clear()
        self.house_input.clear()
        self.type_combo.setCurrentIndex(0)

    
    def save_partner(self):
        if not self.validate_input():
            QMessageBox.warning(self, "Ошибка", "Проверьте правильность заполнения полей", QMessageBox.Ok)
            return
        
        inn = self.inn_input.text()
        name = self.name_input.text()
        type_id = self.type_combo.currentData()
        rating = self.rating_spin.value()
        index = self.index_input.text()
        region = self.region_input.text()
        city = self.city_input.text()
        street = self.street_input.text()
        house = self.house_input.text()
        last_name = self.director_last_name_input.text()
        first_name = self.director_first_name_input.text()
        middle_name = self.director_middle_name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        #self.clear_inputs()
        try:
            if hasattr(self, 'inn') and self.inn:  # Редактирование
                data = (
                    name, type_id, rating, index, region, city,
                    street, house, last_name, first_name, middle_name,
                    phone, email,
                    inn
                )
                update_partner(self.cursor, data)
                QMessageBox.information(None, "Успешно", "Данные партнера обновлены.", QMessageBox.Ok)
            else:
                data = (
                    inn, name, type_id, rating, index, region, city,
                    street, house, last_name, first_name, middle_name,
                    phone, email
                )
                add_partner(self.cursor, data)
                QMessageBox.information(self, "Успешно", "Партнер добавлен.", QMessageBox.Ok)
                self.clear_inputs()

        except Exception as e:
            print(f"Ошибка при сохранении партнера: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось сохранить данные партнера. Подробности: {e}", QMessageBox.Ok)