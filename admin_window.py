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
