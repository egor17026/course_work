import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from firebird.driver import connect, driver_config
from SalaryDB import CreateDatasource


class RDB:
    def __init__(self):
        self.user = 'SYSDBA'
        self.password = 'masterkey'
        self.dbpath = 'localhost:/rdb/kyrsach.fdb'
        self.charset = 'UTF8'

        driver_config.server_defaults.user.value = self.user
        driver_config.server_defaults.password.value = self.password

    def get_connection(self):
        try:
            conn = connect(self.dbpath, charset=self.charset)
            print("Подключение к БД успешно!")
            return conn
        except Exception as e:
            print(f"Ошибка подключения: {e}")
            return None


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.db = CreateDatasource()

        self.ui.check.clicked.connect(self.login)
        self.ui.regist.clicked.connect(self.registracia)

    def login(self):
        login = self.ui.txt_login.text()
        password = self.ui.txt_password.text()

        user_data = self.db.get_user(login)

        if user_data is None:
            print("Пользователь не найден")
            return

        db_hash, is_active, role_id = user_data

        if password == db_hash:
            if is_active == 1:
                print("Успешный вход, ваша роль: {role_id}")
            else:
                print("Аккаунт не подтвержден")
        else:
            print("Невершный пароль, проверьте данные или попробуйте ещё раз")

    def registracia(self):
        print("Кнопка нажата")

if __name__ == "__main__":
    db = RDB()
    conn = db.get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM table_roles")
        for row in cursor.fetchall():
            print(row)
        conn.close()

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
