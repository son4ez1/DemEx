from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidget
)
from PyQt5.uic import loadUi
import sqlite3

from pages.Klient import Klient #менять
from pages.Manager import Manager #менять
from pages.Admin import Admin #менять
from pages.Talon import Talon #менять

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi ("views/welcomescreen.ui", self) # views/welcomeScreen.ui менять
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)  # Password_q из юи ввод пароля менять
        self.SignInButton.clicked.connect(self.registaciya) # Vxod_q из юи вход кнопка менять registaciya функция внизу менять
        
        self.back_Button.clicked.connect(self.back)# back_q из юи нет назад кнопка менять back функция внизу менять
        self.back_Button.hide()# back_q из юи нет назад кнопка менять
        self.AdButton.clicked.connect(self.add)# Add_q из юи добавить  кнопка менять add функция внизу менять
        self.AdButton.hide()# Add_q из юи добавить  кнопка менять

        self.saveButton.hide()# save_q из юи сохранть назад кнопка менять
        self.saveButton.clicked.connect(self.save_func) #save_q из юи сохранть назад кнопка менять и save_func функция внизу менять

        self.stackedWidget.currentChanged.connect(self.hiddenButton) #hiddenButton функция внизу менять

    def save_func(self):
        ID = self.ID.text() #1 id ваше любое название 2-ое из юи где ввод менять (с остальными также)
        print(ID)
        Date_zakaza = self.Date_zakaza.text()
        print(Date_zakaza)
        id_Sostav_tovara = self.id_Sostav_tovara.text()
        print(id_Sostav_tovara)
        Sum = self.Sum.text()
        print(Sum)
        Code_polycheniya = self.Code_polycheniya.text()
        print(Code_polycheniya)
        id_Pynkt_vidachi = self.id_Pynkt_vidachi.text()
        print(id_Pynkt_vidachi)
        id_Terminal = self.Id_Terminal.text()
        print(Id_Terminal)
        id_Klient = self.id_Klient.text()
        print(id_Klient)
       

        conn = sqlite3.connect("Sport.db") #Knizni_club.db менять
        cur = conn.cursor() #создаем переменную для хранения запросов
       
        #Talon МЕНЯТЬ и названия столбцов менять  и то что после VALUES заменить на то, что написано выше
        cur.execute(f'''INSERT INTO Talon (ID, Date_zakaza, id_Sostav_tovara, Sum, Code_polycheniya, id_Pynkt_vidachi, id_Terminal, id_Klient) VALUES ({ID}, "{Date_zakaza}", {id_Sostav_tovara}, "{Sum}", {Code_polycheniya},"{id_Pynkt_vidachi}", {id_Terminal}, {id_Klient}) ''') #получаем тип пользователя, логин и пароль которого был введен
        conn.commit() #сохраняет в подключении запросы
        conn.close() #закрывает подключение



    def registaciya(self):
        login = self.LoginField.text() #Login_q ввод логина из юи менять
        password = self.PasswordField.text() #Password_q ввод пароля из юи менять
       
        if len(login) == 0 or len(password) == 0: #Password_q Login_q менять
            self.ErrorField.setText("Поля должны быть заполнены") #Error_q строка вывода ошибок менять
        else:
            self.ErrorField.setText(" ")#Error_q строка вывода ошибок менять
            conn = sqlite3.connect("Sport.db")#базу менять
            cur = conn.cursor()

            cur.execute(f'SELECT IDavtorizovan FROM Klient where Login = "{login}" and Pass = "{password}"') #Type_atorizovan_id и Klient менять (Login и Password должны быть в таблице)
            typeUser = cur.fetchone() 
           
            if typeUser == None:
                self.ErrorField.setText("Такого пользователя нет") #Error_q строка вывода ошибок менять
            elif typeUser[0] == 1:
                cur.execute(f'SELECT ID FROM Klient WHERE Login = "{login}" and Pass = "{password}"') #id и Klient менять (Login и Password должны быть в таблице)
                typeUs = cur.fetchone()

                self.tableWidget_Klient = self.findChild(QTableWidget, "tableWidget_Klient") #tableWidget_Klient МЕНЯТЬ
                self.stackedWidget.setCurrentWidget(self.Klient) #Klient_q страница из юи менять
                self.lybaya = Klient(self.tableWidget_Klient, typeUs) #Klient это класс из файла который мы создали менять, tableWidget_Klient менять это то где будет выводиться база
                #с остальными пж по примеру 
            elif typeUser[0] == 2:
                self.tableWidget_Manager = self.findChild(QTableWidget, "tableWidget_Manager")
                self.stackedWidget.setCurrentWidget(self.Manager)
                self.lybaya = Manager(self.tableWidget_Manager, typeUs)
            elif typeUser[0] == 3:
                self.tableWidget_Admin = self.findChild(QTableWidget, "tableWidget_Admin")
                self.stackedWidget.setCurrentWidget(self.Admin)
                self.lybaya = Admin(self.tableWidget_Admin, typeUs)
            conn.commit()
            conn.close()
    
    def back(self):
        self.stackedWidget.setCurrentWidget(self.Avtorisation)#Avtorizaciya_q СТРАНица из юи авторизации менчть
        self.lybaya = WelcomeScreen() #WelcomeScreen класс в которым вы щас пишите 
    
    def add(self):
        self.stackedWidget.setCurrentWidget(self.Talon)#AddStoki_q СТРАНица из юи добавление строк менчть
        self.lybaya = Talon() #AddStroki класс добавления строк менять
    
    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Avtorisation:#Avtorizaciya_q СТРАНица из юи авторизации менчть
            self.back_Button.hide()# back_q из юи назад  кнопка менять
            self.AdButton.hide()# Add_q из юи добавить  кнопка менять
        else:
            self.back_Button.show()# back_q из юи назад  кнопка менять
            self.AdButton.show()# Add_q из юи добавить  кнопка менять
        if self.stackedWidget.currentWidget() != self.Talon:#AddStoki_q СТРАНица из юи добавление строк менчть
            self.saveButton.hide()# save_q из юи сохранить  кнопка менять
        else:
            self.saveButton.show()# save_q из юи сохранить  кнопка менять

