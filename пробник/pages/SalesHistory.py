from PyQt5.QtWidgets import ( # 40 шаг: добавляем строчки с 1 по 84
    QDialog, QTableWidgetItem, QTableWidget, QMessageBox, QPushButton)
import math

from pages.db import get_sales_history, get_sales_history_formula
#from EditPartner import EditPartner

class SalesHistory(QDialog):
    def __init__(self, ui, cursor, inn):
        super(SalesHistory, self).__init__()
        self.ui = ui
        self.cursor = cursor
        self.partner_inn = inn
        self.table_widget = self.ui.findChild(QTableWidget, "table_widget")

        self.load_sales_history()  
        self.calculate_material_quantity()

        self.back_btn = self.ui.findChild(QPushButton, "back_btn")
        self.back_btn.clicked.connect(self.back)

    def load_sales_history(self):
        self.table_widget.clearContents()
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Продукт", "Количество", "Дата"])
        
        try:
            sales = get_sales_history(self.cursor, self.partner_inn)
            if not sales:
                QMessageBox.information(None, "История реализации", "У партнера нет истории продаж.", QMessageBox.Ok)
                return

            self.table_widget.setRowCount(len(sales)) #table_widget      sales
            for row, (product_name, quantity, date) in enumerate(sales):
                self.table_widget.setItem(row, 0, QTableWidgetItem(str(product_name))) 
                self.table_widget.setItem(row, 1, QTableWidgetItem(str(quantity)))
                self.table_widget.setItem(row, 2, QTableWidgetItem(str(date)))
                self.table_widget.resizeColumnsToContents()
        except Exception as e:
            print(f"Ошибка при загрузке истории продаж: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось загрузить историю продаж. Подробности: {e}", QMessageBox.Ok)

    def back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageAddPartner) #pageAddPartner
        from pages.EditPartner import EditPartner  # ← импорт внутрь функции
        self.lybaya = EditPartner(self.ui, self.cursor, inn=None)

    def calculate_material_quantity(self):
        try:
            formula_data = get_sales_history_formula(self.cursor, self.partner_inn)

            column_count = self.table_widget.columnCount()

            # Добавим новый столбец, если ещё не добавлен
            if column_count < 4:
                self.table_widget.setColumnCount(4)
                headers = [self.table_widget.horizontalHeaderItem(i).text() for i in range(column_count)]
                headers.append("Количество материала")
                self.table_widget.setHorizontalHeaderLabels(headers)
                self.table_widget.resizeColumnsToContents()

            for row_index in range(self.table_widget.rowCount()):
                if row_index >= len(formula_data):
                    self.table_widget.setItem(row_index, 3, QTableWidgetItem("-1"))
                    continue

                _, koef, quantity, defect_percent = formula_data[row_index]

                if koef is None or quantity is None:
                    total_material = "-1"
                else:
                    defect_percent = defect_percent if defect_percent is not None else 0
                    a = koef * quantity
                    b = a * (defect_percent / 100)
                    total = a + b
                    #total_material = f"{total:.2f}"
                    total_material = math.ceil(total)

                self.table_widget.setItem(row_index, 3, QTableWidgetItem(str(total_material)))

        except Exception as e:
            print(f"Ошибка при расчёте количества материала: {e}")
            QMessageBox.critical(None, "Ошибка", f"Не удалось выполнить расчёт. Подробности: {e}", QMessageBox.Ok)






