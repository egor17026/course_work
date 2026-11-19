# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registration.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Registration(object):
    def setupUi(self, Registration):
        if not Registration.objectName():
            Registration.setObjectName(u"Registration")
        Registration.resize(651, 235)
        self.verticalLayout = QVBoxLayout(Registration)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(Registration)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(Registration)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 15))

        self.verticalLayout.addWidget(self.label)

        self.line_login = QLineEdit(Registration)
        self.line_login.setObjectName(u"line_login")

        self.verticalLayout.addWidget(self.line_login)

        self.label_2 = QLabel(Registration)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 15))

        self.verticalLayout.addWidget(self.label_2)

        self.line_password = QLineEdit(Registration)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.line_password)

        self.btn_register = QPushButton(Registration)
        self.btn_register.setObjectName(u"btn_register")

        self.verticalLayout.addWidget(self.btn_register)

        self.combo_role = QComboBox(Registration)
        self.combo_role.addItem("")
        self.combo_role.addItem("")
        self.combo_role.setObjectName(u"combo_role")

        self.verticalLayout.addWidget(self.combo_role)

        self.line_2 = QFrame(Registration)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)


        self.retranslateUi(Registration)

        QMetaObject.connectSlotsByName(Registration)
    # setupUi

    def retranslateUi(self, Registration):
        Registration.setWindowTitle(QCoreApplication.translate("Registration", u"Registration", None))
        self.label.setText(QCoreApplication.translate("Registration", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Registration", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_register.setText(QCoreApplication.translate("Registration", u"\u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.combo_role.setItemText(0, QCoreApplication.translate("Registration", u"\u041a\u0430\u0434\u0440\u043e\u0432\u0438\u043a", None))
        self.combo_role.setItemText(1, QCoreApplication.translate("Registration", u"\u0411\u0443\u0433\u0445\u0430\u043b\u0442\u0435\u0440", None))

    # retranslateUi

