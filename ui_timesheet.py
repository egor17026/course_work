# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timesheet.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(602, 564)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label)

        self.line_date = QLineEdit(Form)
        self.line_date.setObjectName(u"line_date")

        self.verticalLayout.addWidget(self.line_date)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_2)

        self.combo_shift = QComboBox(Form)
        self.combo_shift.setObjectName(u"combo_shift")

        self.verticalLayout.addWidget(self.combo_shift)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_4)

        self.combo_worker = QComboBox(Form)
        self.combo_worker.setObjectName(u"combo_worker")

        self.verticalLayout.addWidget(self.combo_worker)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_3)

        self.line_hours = QLineEdit(Form)
        self.line_hours.setObjectName(u"line_hours")

        self.verticalLayout.addWidget(self.line_hours)

        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")

        self.verticalLayout.addWidget(self.btn_save)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043c\u0435\u043d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0440\u0430\u0431\u043e\u0442\u043d\u0438\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0427\u0430\u0441\u044b \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.btn_save.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

