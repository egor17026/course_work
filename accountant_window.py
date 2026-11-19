from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QInputDialog
from ui_accwindow import Ui_AccWindow
from SalaryDB import CreateDatasource

class AccountantWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AccWindow()
        self.ui.setupUi(self)

        self.db = CreateDatasource()

        self.load_workers()
        self.load_payroll()

        self.ui.btn_calc.clicked.connect(self.calculate)
        self.ui.btn_logout.clicked.connect(self.logout)

    def load_workers(self):
        workers = self.db.get_all_workers()
        self.ui.table_workers.setRowCount(len(workers))

        for row_idx, worker in enumerate(workers):
            worker_id, last_name, first_name, middle_name, position, department, status = worker
            fio = f"{last_name} {first_name} {middle_name}"

            self.ui.table_workers.setItem(row_idx, 0, QTableWidgetItem(str(worker_id)))
            self.ui.table_workers.setItem(row_idx, 1, QTableWidgetItem(fio))
            self.ui.table_workers.setItem(row_idx, 2, QTableWidgetItem(str(position)))

    def load_payroll(self):
        records = self.db.get_payroll_history()
        self.ui.table_payroll.setRowCount(len(records))
        self.ui.table_payroll.setColumnCount(7)
        self.ui.table_payroll.setHorizontalHeaderLabels(["ID", "Фамилия", "Имя", "Месяц", "Начислено", "Налог", "К выплате"])

        for row_idx, record in enumerate(records):
            for col_idx, value in enumerate(record):
                self.ui.table_payroll.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def calculate(self):
        current_row = self.ui.table_workers.currentRow()
        if current_row == -1:
            print("Выберите работника")
            return

        worker_id = int(self.ui.table_workers.item(current_row, 0).text())

        month, ok = QInputDialog.getText(self, "Расчет", "Введите месяц:")
        if not ok or not month:
            return

        # Вызываем метод базы
        result = self.db.calc_salary_and_save(worker_id, month)

        if result:
            gross, tax, net = result
            QMessageBox.information(self, "Успех", f"Начислено: {gross}\nНалог: {tax}\nК выплате: {net}")
            self.load_payroll()
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось рассчитать (возможно, нет смен за этот месяц).")

    def logout(self):
        from widget import Widget
        self.login_win = Widget()
        self.login_win.show()
        self.close()
