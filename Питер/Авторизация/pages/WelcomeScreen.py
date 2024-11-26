#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, 
    QTableWidget # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

from pages.StarshiSmeni import StarshiSmeni
from pages.Administrator import Administrator
from pages.Prodavez import Prodavez

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

        conn = sqlite3.connect("piter.db") # подключение к бд
        cur = conn.cursor() # создаем переменную для хранения запроса
        #cur.execute(f''' insert INTO requests 
        #(IDrequest, startDate, orgTechTypeID, orgTechModel, problemDescryption, requestStatusID, completionDate, repairParts, masterID, clientID) 
        #VALUES (8, "2023-09-10", 1, "Dsrk.xftncz", "Выключается", 3, "2023-05-23", "2023-05-23", 2, 7); 
        #''') # получаем тип пользователя, логин и пароль которого был введен
        print ("готово")
        conn.commit() #сохраняет в подключении запросы
        conn.close() # закрывает подключение

    def signupfunction(self): # создаем функцию регистрации
        
        user = self.LoginField.text() # создаем пользователя и получаем из поля ввода логина введенный текст
        password = self.PasswordField.text() # создаем пароль и получаем из поля ввода пароля введенный текст
        print(user, password) # выводит логин и пароль

        if len(user)==0 or len(password)==0: # если пользователь оставил пустые поля
            self.ErrorField.setText("Заполните все поля") # выводим ошибку в поле
        else:
            self.ErrorField.setText("Все ок") # выводим что все хорошо в поле

            conn = sqlite3.connect("piter.db") # подключение к базе данных в () изменить на название своей БД
            cur = conn.cursor() # переменная для запросов

            cur.execute('SELECT dolzhnosti FROM sotrudniki WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
            typeUser = cur.fetchone() # получает только один тип пользователя
            #print(typeUser[0]) # выводит тип пользователя без скобок       
            if typeUser == None:
                self.ErrorField.setText("Такого пользователя нет в базе")
            elif typeUser[0] == 2:
                cur.execute('SELECT ID FROM sotrudniki WHERE login=(?) and password=(?)', [user, password]) # получаем тип пользователя, логин и пароль которого был введен
                typeAdministrator = cur.fetchone() # получает только один тип пользователя

                self.tableWidget_Administrator = self.findChild(QTableWidget, "tableWidget_Administrator")
                self.stackedWidget.setCurrentWidget(self.Administrator)
                self.lybaya = Administrator(self.tableWidget_Administrator, typeAdministrator)
            elif typeUser[0] == 3:
                self.tableWidget_StarshiSmeni = self.findChild(QTableWidget, "tableWidget_StarshiSmeni") # находит в приложении нужную таблицу
                self.stackedWidget.setCurrentWidget(self.StarshiSmeni)
                self.lybaya = StarshiSmeni(self.tableWidget_StarshiSmeni)
            elif typeUser[0] == 1:
                self.tableWidget_Prodavez = self.findChild(QTableWidget, "tableWidget_Prodavez") 
                self.stackedWidget.setCurrentWidget(self.Prodavez)
                self.lybaya = Prodavez(self.tableWidget_Prodavez)


            conn.commit() # сохраняет в подключении запросы
            conn.close() # закрываем подключение

    def backs(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)
        self.lybaya = WelcomeScreen()
        print("ok")


    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Avtorisation:  
            self.back_Button.hide() #скрыть кнопку назад
            self.AdButton.hide() #скрыть кнопку добавить
        else:
            self.back_Button.show()
            self.AdButton.show()





