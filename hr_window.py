from PySide6.QtWidgets import QWidget, QTableWidgetItem
from SalaryDB import CreateDatasource
from ui_hrwindow import Ui_Form
from add_worker_window import AddWorkerWindow

class HRWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = CreateDatasource()
        self.load_workers()

        self.ui.btn_add.clicked.connect(self.add_worker_click)
        self.ui.btn_fire.clicked.connect(self.fire_worker_click)

    def load_workers(self):
        workers = self.db.get_all_workers()
        self.ui.tableWidget.setRowCount(len(workers))

        for row_idx, worker in enumerate(workers):
            worker_id, last_name, first_name, middle_name, position, department, status = worker
            fio = f"{last_name} {first_name} {middle_name}"

            self.ui.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(worker_id)))
            self.ui.tableWidget.setItem(row_idx, 1, QTableWidgetItem(fio))
            self.ui.tableWidget.setItem(row_idx, 2, QTableWidgetItem(str(position)))
            self.ui.tableWidget.setItem(row_idx, 3, QTableWidgetItem(str(department)))
            self.ui.tableWidget.setItem(row_idx, 4, QTableWidgetItem(str(status)))

    def fire_worker_click(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row == -1:
            print("Выберите работника на увольнение")
            return
        worker_id_item = self.ui.tableWidget.item(current_row, 0)
        if worker_id_item is not None:
            worker_id = int(worker_id_item.text())

            if self.db.request_fire_worker(worker_id):
                print(f"Запрос на увольнение работника - {worker_id} отправлен админу")
                self.load_workers()

    def add_worker_click(self):
        self.add_win = AddWorkerWindow()
        self.add_win.show()
