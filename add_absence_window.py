from PySide6.QtWidgets import QWidget, QMessageBox
from ui_add_vacation_sick import Ui_Form
from SalaryDB import CreateDatasource

class AddAbsenceWindow(QWidget):
    def __init__(self, worker_id):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = CreateDatasource()
        self.worker_id = worker_id

        self.ui.btn_save.clicked.connect(self.save_data)

    def save_data(self):
        date_start = self.ui.line_start.text()
        date_end = self.ui.line_end.text()
        list_number = self.ui.line_list.text()

        type_text = self.ui.combo_type.currentText()

        if not date_start or not date_end:
            QMessageBox.warning(self, "Ошибка", "Введите даты (ГГГГ-ММ-ДД)!")
            return

        if "больничн" in type_text.lower():
            if self.db.add_sick_leaves(self.worker_id, date_start, date_end, list_number):
                QMessageBox.information(self, "Успех", "Больничный оформлен!")
                self.close()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось оформить больничный.")
        else:
            if self.db.add_vacation(self.worker_id, date_start, date_end, type_text):
                QMessageBox.information(self, "Успех", "Отпуск оформлен!")
                self.close()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось оформить отпуск.")
