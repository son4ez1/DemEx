from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog,
    QTableWidgetItem # это базовый класс диалогового окна
)

from PyQt5.uic import loadUi # загрузка интерфейса, созданного в Qt Creator

import sqlite3

class Master(QDialog):
    def __init__(self, tadle , typeMaster):        
        super(Master, self).__init__()
        print("ok")
        self.tableWidget_Master = tadle
        print(tadle)
        self.vivod(typeMaster)

    def vivod(self,typeMaster):
        conn = sqlite3.connect("../бд/uchet.db") # подключение к бд
        cur = conn.cursor() # создаем переменную для хранения запроса
        zayavki=cur.execute(f'''  SELECT 
        r.IDrequest as "номер заявки",
        r.startDate as "дата начала",
        ott.orgTechType as "тип организациии",
        r.orgTechModel as "модель",
        r.problemDescryption as "проблема",
        rs.requestStatus as "статус заявки",
        r.completionDate as "дата окончания",
        r.repairParts as "детали для ремонта",
        us.fio as "мастер",
        usr.fio as "клиент",
        com.message as "коментарии"
        FROM requests r 
        LEFT JOIN 
        orgTechTypes ott on r.orgTechTypeID = ott.IDorgTechType
        left join 
        requestStatuses rs on r.requestStatusID = rs.IDrequestStatus
        left join 
        users us on r.masterID = us.IDuser
        left join
        users usr on r.clientID = usr.IDuser
        left join 
        comments com on r.IDrequest = com.requestID
        where r.masterID = "{typeMaster[0]}"
        ''') # получаем тип пользователя, логин и пароль которого был введен
        print (zayavki)
        name_stolba = [xz[0] for xz in zayavki.description] #вывод названия столбцов
        print(name_stolba)

        self.tableWidget_Master.setColumnCount(len(name_stolba)) # считает количество столбцов
        self.tableWidget_Master.setHorizontalHeaderLabels(name_stolba) # вместо цифр подставляет название столбцов

        dan_table = cur.fetchall() # получает все данные из бд, но онине структурированы
        self.tableWidget_Master.setRowCount(0)# убирает добавление пустых строк
        # row - строки
        for i, row in enumerate(dan_table): # цикл по строчкам
            self.tableWidget_Master.setRowCount(self.tableWidget_Master.rowCount() + 1) # добавил пустые строки в нужном количестве
            for l, cow in enumerate(row): # по ячейкам заносит данные
                self.tableWidget_Master.setItem(i,l, QTableWidgetItem(str(cow))) 
        print(dan_table)

        self.tableWidget_Master.resizeColumnsToContents() # столбцы стал по размеру данных


        conn.commit() #сохраняет в подключении запросы
        conn.close() # закрывает подключение
