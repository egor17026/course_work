from PySide6.QtWidgets import QWidget, QMessageBox
from ui_registration import Ui_Registration
from SalaryDB import CreateDatasource

class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)

        self.db = CreateDatasource()

        self.ui.btn_register.clicked.connect(self.register)

    def register(self):
        login = self.ui.line_login.text()
        password = self.ui.line_password.text()
        role_name = self.ui.combo_role.currentText()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните логин и пароль!")
            return

        role_id = 2 if role_name == "Кадровик" else 3

        if self.db.register_user(login, password, role_id):
            QMessageBox.information(self, "Успех", "Заявка отправлена!\nОжидайте подтверждения администратора.")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось зарегистрироваться.\nВозможно, такой логин уже существует.")
