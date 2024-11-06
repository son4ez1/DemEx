#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, 
    QTableWidget # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

from pages.Zakazchik import Zakazchik
from pages.Master import Master
from pages.Operator import Operator
from pages.Manager import Manager

# Окно приветствия
class WelcomeScreen(QDialog):
    """
    Это класс окна приветствия.
    """
    def __init__(self):
        """
        Это конструктор класса
        """
        super(WelcomeScreen, self).__init__()
        loadUi("views/welcomescreen.ui",self) # загружаем интерфейс.
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password) # скрываем пароль
        self.SignInButton.clicked.connect(self.signupfunction) # нажати на кнопку и вызов функции
        self.back_Button.clicked.connect(self.backs)
        self.back_Button.hide()
        self.stackedWidget.currentChanged.connect(self.hiddenButton)
        # Подключение кнопок к методам переключения страниц с использованием lambda
        #self.SignInButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Zakazchik))

    def signupfunction(self): # создаем функцию регистрации
        
        user = self.LoginField.text() # создаем пользователя и получаем из поля ввода логина введенный текст
        password = self.PasswordField.text() # создаем пароль и получаем из поля ввода пароля введенный текст
        print(user, password) # выводит логин и пароль

        if len(user)==0 or len(password)==0: # если пользователь оставил пустые поля
            self.ErrorField.setText("Заполните все поля") # выводим ошибку в поле
        else:
            self.ErrorField.setText("Все ок") # выводим что все хорошо в поле

            conn = sqlite3.connect("uchet.db") # подключение к базе данных в () изменить на название своей БД
            cur = conn.cursor() # переменная для запросов

            cur.execute('SELECT typeID FROM users WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
            typeUser = cur.fetchone() # получает только один тип пользователя
            #print(typeUser[0]) # выводит тип пользователя без скобок       
            if typeUser == None:
                self.ErrorField.setText("Такого пользователя нет в базе")
            elif typeUser[0] == 4:
                cur.execute('SELECT IDuser FROM users WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
                typeZakazchik = cur.fetchone() # получает только один тип пользователя

                self.tableWidget_Zakazchik = self.findChild(QTableWidget, "tableWidget_Zakazchik")
                self.stackedWidget.setCurrentWidget(self.Zakazchik)
                self.lybaya = Zakazchik(self.tableWidget_Zakazchik, typeZakazchik)
            elif typeUser[0] == 2:
                cur.execute('SELECT IDuser FROM users WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
                typeMaster = cur.fetchone() # получает только один тип пользователя
            
                self.tableWidget_Master = self.findChild(QTableWidget, "tableWidget_Master")
                self.stackedWidget.setCurrentWidget(self.Master)
                self.lybaya = Master(self.tableWidget_Master, typeMaster)
            elif typeUser[0] == 3:
                self.tableWidget_Operator = self.findChild(QTableWidget, "tableWidget_Operator") # находит в приложении нужную таблицу
                self.stackedWidget.setCurrentWidget(self.Operator)
                self.lybaya = Operator(self.tableWidget_Operator)
            elif typeUser[0] == 1:
                self.tableWidget_Manager = self.findChild(QTableWidget, "tableWidget_Manager") 
                self.stackedWidget.setCurrentWidget(self.Manager)
                self.lybaya = Manager(self.tableWidget_Manager)


            conn.commit() # сохраняет в подключении запросы
            conn.close() # закрываем подключение

    def backs(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)
        self.lybaya = WelcomeScreen()
        print("ok")

    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Avtorisation:  
            self.back_Button.hide()
        else:
            self.back_Button.show()



