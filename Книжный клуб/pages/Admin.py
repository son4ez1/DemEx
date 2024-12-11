from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidgetItem
)
from PyQt5.uic import loadUi
import sqlite3


class Admin (QDialog):
    def __init__(self, table, typeUs): #[1]- типо сноски typeUs менять из WelcomeScreen
        super(Admin, self).__init__()
        self.tableWidget_Admin = table #tableWidget_Klient менять 
        self.vivod(typeUs)

    def vivod(self, typeUs):
        conn = sqlite3.connect("KnizhniClub.db") #Knizni_club.db менять
        cur = conn.cursor()
        #запрос менять
        zayavki = cur.execute(f'''SELECT  
        t.ID as "Номер заказа", 
        t.Date_zakaza as "Дата заказа",
        tov.Naimenovanie as "Наименование товара",
        t.Sum as "Сумма товаров",
        t.Code_polycheniya as "Код получения",
        p.Adress as "Пункт выдачи",
        ter.Adress as "Адрес терминалa",
        termin.Name_TC as "ТЦ Терминала",
        k.FIO as "ФИО клиента"
        FROM Talon t

        LEFT JOIN
        Sostav_tovara s on t.id_Sostav_tovara = s.ID_code
        LEFT JOIN
        Tovar tov on s.id_tovara = tov.ID

        left join 
        PVZ p on t.id_Pynkt_vidachi = p.ID
        left JOIN
        Terminal ter on t.Id_Terminal = ter.ID
        LEFT JOIN
        Terminal termin on t.Id_Terminal = termin.ID
        LEFT JOIN
        Klient k on t.id_Klient = k.ID
        where t.id_Klient = "{typeUs[0]}"''')

        name_stolba = [xz[0] for xz in zayavki.description] 
        print(name_stolba)

        self.tableWidget_Admin.setColumnCount(len(name_stolba)) #tableWidget_Klient менять
        self.tableWidget_Admin.setHorizontalHeaderLabels(name_stolba) #tableWidget_Klient менять

        dan_table= cur.fetchall()
        
        self.tableWidget_Admin.setRowCount(0) #tableWidget_Klient менять
        # row - строки
        for i, row in enumerate(dan_table): #цикл по строкам
            self.tableWidget_Admin.setRowCount(self.tableWidget_Admin.rowCount() + 1) #tableWidget_Klient менять
            for l, cow in enumerate(row): #начинает по ячейке заносить данные
                self.tableWidget_Admin.setItem(i,l,QTableWidgetItem(str(cow))) #tableWidget_Klient менять
        print(dan_table)

        self.tableWidget_Admin.resizeColumnsToContents() #tableWidget_Klient менять

        conn.commit()
        conn.close()

   

        
    
   