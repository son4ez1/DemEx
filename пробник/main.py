from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QListWidget
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.uic import loadUi
import sys # 1 шаг: добавляем строчки с 1 по 5
from pages.db import connect_db # 7 шаг: добавляем строчку 6
from pages.PartnersView import PartnersView # 10 шаг: добавляем строчку 7

class MainWindow(QDialog):

    def __init__(self):
        """
        Создаём PartnersView, передаём весь self и cursor.
        """
        super(MainWindow, self).__init__()
        loadUi("views/dialog.ui", self) # 2 шаг: добавляем строчки с 9 по 16
        self.conn, self.cursor = connect_db() # 8 шаг: добавляем строчку 17
        self.btnBack.clicked.connect(self.go_back) # 32 шаг: добавляем строчки с 18 по 20(запускаем)
        self.btnBack.hide()
        self.stackedWidget.currentChanged.connect(self.hiddenButton)

        self.partners_view = PartnersView(self, self.cursor) # 9 шаг: добавляем строчку 22
        self.partners_view.load_partners()

    def go_back(self):# 31 шаг: добавляем строчки с 25 по 32
        self.stackedWidget.setCurrentWidget(self.Partners)  #pagePartners - название странице где вывояься партнеры
    
    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Partners:
            self.btnBack.hide() #btnBack - кнопка назад на главном окне 
        else:
            self.btnBack.show() #btnBack - кнопка назад на главном окне 


if __name__ == "__main__": # 3 шаг: добавляем строчки с 35 по 48 (запускаем приложение)
    app = QApplication(sys.argv)

    icon = QIcon()
    icon.addPixmap(QPixmap("media/search_book_open_search_locate_6178.png"), QIcon.Normal, QIcon.Off)
    app.setWindowIcon(icon)

    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Вы закрыли приложение")

