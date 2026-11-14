# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hr_menu.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(774, 581)
        self.btn_workers = QPushButton(Form)
        self.btn_workers.setObjectName(u"btn_workers")
        self.btn_workers.setGeometry(QRect(10, 10, 251, 31))
        self.btn_orders = QPushButton(Form)
        self.btn_orders.setObjectName(u"btn_orders")
        self.btn_orders.setGeometry(QRect(510, 10, 251, 31))
        self.btn_timesheet = QPushButton(Form)
        self.btn_timesheet.setObjectName(u"btn_timesheet")
        self.btn_timesheet.setGeometry(QRect(260, 10, 251, 31))
        self.btn_logout = QPushButton(Form)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(642, 530, 121, 36))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_workers.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u043e\u0432", None))
        self.btn_orders.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043a\u0430\u0437\u044b", None))
        self.btn_timesheet.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0431\u0435\u043b\u044c", None))
        self.btn_logout.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

