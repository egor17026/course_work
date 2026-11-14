from PySide6.QtWidgets import QWidget, QTableWidgetItem
from SalaryDB import CreateDatasource
from ui_accwindow import Ui_Form

class AccountantWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = CreateDatasource()

        self.ui.btn_logout.clicked.connect(self.logout)

        self.load_workers()

    def load_workers(self):
        workers = self.db.get_all_workers()
        self.ui.tableWidget.setRowCount(len(workers))

        for row_idx, worker in enumerate(workers):
            worker_id, last_name, first_name, middle_name, position, department, status = worker
            fio = f"{last_name} {first_name} {middle_name}"

            self.ui.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(worker_id)))
            self.ui.tableWidget.setItem(row_idx, 1, QTableWidgetItem(fio))
            self.ui.tableWidget.setItem(row_idx, 2, QTableWidgetItem(str(position)))

    def logout(self):
        from widget import Widget
        self.login_win = Widget()
        self.login_win.show()
        self.close()
