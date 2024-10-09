
#  widget - это имя, присваиваемое компоненту пользовательского интерфейса,
#  с которым пользователь может взаимодействовать 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, # это то, что поддерживает работоспособность приложения Qt, выполняя его основной цикл событий
    QDialog # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sys # взаимодействие с интерпретатором

from PyQt5.QtGui import QPixmap, QIcon # для работы с изображениями и загрузки иконок

import sqlite3 
 
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("dialog.ui",self) # загружаем интерфейс
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password) # скрывает пароль
        self.SigninButton.clicked.connect(self.Vxod) # кнопка входа

    def Vxod (self): # кнопка входа
        print ("вход")
        user = self.LoginField.text() # ввод текста в логин
        pwd = self.PasswordField.text() # ввод текста в пароль
        #userinfo = [user, pwd]  

        if user == "" or pwd == "": # вывод ошибки
            self.ErrorField.setText("Заполните все поля")
        else:
            print (user,pwd)
            conn = sqlite3.connect("бд/uchet.db") #подключение бд
            cur = conn.cursor() # подключили элемент бд
            cur.execute("select typeID from users where login = ? and password = ?", (user, pwd)) #выводим айдишник пользователя
            #cur.execute("select * from users where login = 'login1' and password = 'pass1'")
            typeuser = cur.fetchone()
            print(typeuser[0]) # выводим цифру без скобок
            if typeuser[0] == 1: # если зашел менеджер, открываем окно менеджера
                print ("test")
                manager = Manager()
                widget.addWidget(manager)
                widget.setCurrentIndex(widget.currentIndex() + 1) # открыть еще одно окно
            conn.commit() # сохранение для бд
            conn.close()# закрытие для бд

class Manager(QDialog): #открываем другую страницу
    def __init__(self):
        super(Manager, self).__init__()
        loadUi("manager.ui",self) # загружаем интерфейс


app = QApplication(sys.argv)

# позволят менять страницы в окне
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)

# загружаем иконку
icon = QIcon()
icon.addPixmap(QPixmap("logo.png"), QIcon.Normal, QIcon.Off)
widget.setWindowIcon(icon) 
widget.show()
# запускаем приложение
try:
    sys.exit(app.exec_())
except:
    print("You close application")


