from PySide6.QtWidgets import QWidget, QTableWidgetItem
from ui_adminwindow import Ui_AdminWindow
from SalaryDB import CreateDatasource  # Импортируем базу

class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        print("Окно администратора успешно открыто!")

        self.db = CreateDatasource()

        self.ui.Confirm.clicked.connect(self.confirm_user)

        self.load_users()

        self.load_pending_workers()

        self.ui.btn_approve_hire.clicked.connect(self.approve_hire)
        self.ui.btn_approve_fire.clicked.connect(self.approve_fire)

        self.ui.btn_add_dept.clicked.connect(self.add_department_click)
        self.ui.btn_add_pos.clicked.connect(self.add_position_click)

        self.ui.btn_logout.clicked.connect(self.logout)

    def load_users(self):
        users = self.db.get_all_users()

        self.ui.tableWidget.setRowCount(len(users))

        for row_idx, user in enumerate(users):
            user_id, login, is_active = user

            self.ui.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(user_id)))
            self.ui.tableWidget.setItem(row_idx, 1, QTableWidgetItem(str(login)))

            status_text = "Активен" if is_active == 1 else "В ожидании"
            self.ui.tableWidget.setItem(row_idx, 2, QTableWidgetItem(status_text))
    def confirm_user(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row == -1:
            print("Выберите пользователя")
            return
        user_id_item = self.ui.tableWidget.item(current_row, 0)
        if user_id_item is not None:
            user_id = int(user_id_item.text())
        self.db.activate_user(user_id)
        self.load_users()

    def load_pending_workers(self):
        workers = self.db.get_pending_workers()
        self.ui.table_workers.setRowCount(len(workers))
        self.ui.table_workers.setColumnCount(3)
        self.ui.table_workers.setHorizontalHeaderLabels(["ID", "ФИО", "Статус"])

        for row_idx, worker in enumerate(workers):
            worker_id, last_name, first_name, middle_name, status = worker
            fio = f"{last_name} {first_name} {middle_name}"

            self.ui.table_workers.setItem(row_idx, 0, QTableWidgetItem(str(worker_id)))
            self.ui.table_workers.setItem(row_idx, 1, QTableWidgetItem(fio))
            self.ui.table_workers.setItem(row_idx, 2, QTableWidgetItem(str(status)))

    def approve_hire(self):
        current_row = self.ui.table_workers.currentRow()
        if current_row == -1:
            print("Выберите работника")
            return

        worker_id = int(self.ui.table_workers.item(current_row, 0).text())
        if self.db.approve_hire_worker(worker_id):
            print("Прием подтвержден!")
            self.load_pending_workers()

    def approve_fire(self):
        current_row = self.ui.table_workers.currentRow()
        if current_row == -1:
            print("Выберите работника")
            return

        worker_id = int(self.ui.table_workers.item(current_row, 0).text())
        if self.db.approve_fire_worker(worker_id):
            print("Увольнение подтверждено!")
            self.load_pending_workers()

    def add_department_click(self):
        name = self.ui.line_dept_name.text()
        if not name:
            print("Введите название отдела")
            return
        if self.db.add_department(name):
            print("Отдел добавлен!")
            self.ui.line_dept_name.clear()

    def add_position_click(self):
        name = self.ui.line_pos_name.text()
        oklad = self.ui.line_oklad.text()
        rate = self.ui.line_rate.text()

        if not name:
            print("Введите название должности")
            return
        if self.db.add_position(name, oklad, rate):
            print("Должность добавлена!")
            self.ui.line_pos_name.clear()
            self.ui.line_oklad.clear()
            self.ui.line_rate.clear()

    def logout(self):
        from widget import Widget
        self.login_win = Widget()
        self.login_win.show()
        self.close()
