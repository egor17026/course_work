from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton

class Ui_Registration(object):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(400, 300)

        self.verticalLayout = QVBoxLayout(Registration)

        self.label_login = QLabel("Логин")
        self.verticalLayout.addWidget(self.label_login)

        self.line_login = QLineEdit()
        self.verticalLayout.addWidget(self.line_login)

        self.label_password = QLabel("Пароль")
        self.verticalLayout.addWidget(self.label_password)

        self.line_password = QLineEdit()
        self.line_password.setEchoMode(QLineEdit.Password)
        self.verticalLayout.addWidget(self.line_password)

        self.label_role = QLabel("Роль")
        self.verticalLayout.addWidget(self.label_role)

        self.combo_role = QComboBox()
        self.combo_role.addItem("Кадровик")
        self.combo_role.addItem("Бухгалтер")
        self.verticalLayout.addWidget(self.combo_role)

        self.btn_register = QPushButton("Зарегистрироваться")
        self.verticalLayout.addWidget(self.btn_register)

        self.retranslateUi(Registration)
        QMetaObject.connectSlotsByName(Registration)

    def retranslateUi(self, Registration):
        Registration.setWindowTitle("Регистрация")
