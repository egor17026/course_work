from PySide6.QtWidgets import QWidget, QMessageBox
from ui_timesheet import Ui_Form
from SalaryDB import CreateDatasource

class TimesheetWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = CreateDatasource()
        self.load_workers()

        self.ui.combo_shift.addItem("Явка", "явка")
        self.ui.combo_shift.addItem("Отпуск", "отпуск")
        self.ui.combo_shift.addItem("Больничный", "больничный")
        self.ui.combo_shift.addItem("Прогул", "прогул")

        self.ui.btn_save.clicked.connect(self.save_timesheet)

    def load_workers(self):
        workers = self.db.get_all_workers()
        for worker in workers:
            worker_id = worker[0]
            fio = f"{worker[1]} {worker[2]}"
            self.ui.combo_worker.addItem(fio, worker_id)

    def save_timesheet(self):
        worker_id = self.ui.combo_worker.currentData()
        work_date = self.ui.line_date.text()
        shift_type = self.ui.combo_shift.currentData()
        hours_worked = self.ui.line_hours.text()

        if not work_date or not hours_worked:
            QMessageBox.warning(self, "Ошибка", "Заполните дату и часы!")
            return

        if self.db.add_timesheet(worker_id, work_date, shift_type, hours_worked):
            QMessageBox.information(self, "Успех", "Смена зафиксирована!")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось сохранить.")
