# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hr_orders.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(649, 555)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table = QTabWidget(Form)
        self.table.setObjectName(u"table")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_vacations = QTableWidget(self.widget)
        self.table_vacations.setObjectName(u"table_vacations")

        self.verticalLayout.addWidget(self.table_vacations)

        self.table.addTab(self.widget, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_sicks = QTableWidget(self.tab_2)
        self.table_sicks.setObjectName(u"table_sicks")

        self.verticalLayout_2.addWidget(self.table_sicks)

        self.table.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.table)


        self.retranslateUi(Form)

        self.table.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.table.setTabText(self.table.indexOf(self.widget), QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0443\u0441\u043a\u0430", None))
        self.table.setTabText(self.table.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u0411\u043e\u043b\u044c\u043d\u0438\u0447\u043d\u044b\u0435", None))
    # retranslateUi

