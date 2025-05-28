from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QLabel, QMessageBox, QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore # 4 шаг: добавляем строчки с 1 по 3
from pages.db import get_partners # 13 шаг: добавляем строчку 4
from pages.AddPartner import AddPartner # 18 шаг: добавляем строчку 5
from pages.EditPartner import EditPartner # 36 шаг: добавляем строчку 6

class PartnersView:
    def __init__(self, ui, cursor):
        super(PartnersView, self).__init__()
        self.ui = ui
        self.cursor = cursor # 5 шаг: добавляем строчки с 8 по 12

        self.btnSave = self.ui.findChild(QPushButton, "btnSave") # 19 шаг: добавляем строчки с 14 по 16
        self.btnHistory = self.ui.findChild(QPushButton, "btnHistory")
        self.Add_button = self.ui.findChild(QPushButton, "Add_button")

        self.VivodParynera = self.ui.findChild(QListWidget, "VivodParynera") # 14 шаг: добавляем строчку 18 (запускаем(если ошибка,меняем индексы))
        self.btn_add = self.ui.findChild(QPushButton, "btnAddPartner") # 25 шаг: добавляем строчки 19 и 21 (запускаем)

        self.btn_add.clicked.connect(self.add_partner)
        self.VivodParynera.itemClicked.connect(self.show_partner_details) # 37 шаг: добавляем строчку 22 (запускаем)
        self.ui.stackedWidget.currentChanged.connect(self.on_page_changed)# 30 шаг: добавляем строчки с 23 по 28
      
    def on_page_changed(self, index): # 30 шаг: добавляем строчки с 23 по 28
        current_widget = self.ui.stackedWidget.widget(index)
        if current_widget == self.ui.Partners:
            self.load_partners()

    def load_partners(self): # 11 шаг: добавляем строчки с 30 по 96
        try:
            partners = get_partners(self.cursor) #get_partners - название функции в db.py 
            if not partners:
                QMessageBox.warning(None, "Предупреждение", "Партнёры не найдены.", QMessageBox.Ok)
                return
            
            self.VivodParynera.clear()

            for partner in partners:
                inn, html = self.format_partner_info(partner)
                item = QListWidgetItem()
                label = QLabel()
                label.setText(html)
                label.setWordWrap(True)
                label.setTextFormat(Qt.RichText)
                label.adjustSize()
                item.setSizeHint(QSize(label.width(), label.height() + 20))
                item.setData(QtCore.Qt.UserRole, inn)
                self.VivodParynera.addItem(item)
                self.VivodParynera.setItemWidget(item, label)
                label.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)

        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка загрузки: {e}", QMessageBox.Ok)
        

    def format_partner_info(self, partner): #тут менять названия столбцов если другая база inn, tip.....
        inn = partner[0]
        tip = partner[2]
        name = partner[1]
        total_quantity = partner[3] if partner[3] else 0
        telefon = partner[8] or "Телефон не указан"
        rejting = partner[4]
        director = f"{partner[5]} {partner[6]} {partner[7]}".strip() or "Директор не указан"
        discount = self.calculate_discount(total_quantity) #total_quantity-столбец с итоговой суммой 

        html = f"""
        <div style='font-size: 14pt;'>
            <table width='100%'>
                <tr>
                    <td style='width: 70%;'><b>{tip}</b> | {name}</td>
                    <td style='width: 30%; text-align: right;'>
                        <span style='color:#333;'>{discount}%</span>
                    </td>
                </tr>
            </table>
        </div>
        <div style='font-size: 10pt; color:#666; margin-top: 8px; line-height: 1.4;'>
            <div>{director}</div>
            <div>{telefon}</div>
            <div>Рейтинг: {rejting}</div>
            <div>.</div>
            <div></div>
        </div>
        """
        return inn, html
    
    def calculate_discount(self, quantity):
        if quantity < 10000:
            return 0
        elif quantity < 50000:
            return 5
        elif quantity < 300000:
            return 10
        else:
            return 15
        
    def add_partner(self): # 15 шаг: добавляем строчки с 98 по 103
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageAddPartner) #pageAddPartner - страница с олями где обавление партнера
        self.lybaya = AddPartner(self.ui, self.cursor)
        self.btnSave.hide()
        self.btnHistory.hide()
        self.Add_button.show()

    def show_partner_details(self, item): # 33 шаг: добавляем строчки с 105 по 112
        inn = item.data(QtCore.Qt.UserRole)
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageAddPartner)#pageAddPartner - страница с олями где обавление партнера
        self.lybaya = EditPartner(self.ui, self.cursor, inn)

        self.btnSave.show()
        self.btnHistory.show()
        self.Add_button.hide()