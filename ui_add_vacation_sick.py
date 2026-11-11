# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_vacation_sick.ui'
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
        Form.resize(856, 728)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label)

        self.line_start = QLineEdit(Form)
        self.line_start.setObjectName(u"line_start")

        self.verticalLayout.addWidget(self.line_start)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_2)

        self.line_end = QLineEdit(Form)
        self.line_end.setObjectName(u"line_end")

        self.verticalLayout.addWidget(self.line_end)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_3)

        self.line_list = QLineEdit(Form)
        self.line_list.setObjectName(u"line_list")

        self.verticalLayout.addWidget(self.line_list)

        self.combo_type = QComboBox(Form)
        self.combo_type.addItem("")
        self.combo_type.addItem("")
        self.combo_type.addItem("")
        self.combo_type.setObjectName(u"combo_type")

        self.verticalLayout.addWidget(self.combo_type)

        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")

        self.verticalLayout.addWidget(self.btn_save)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u043b\u043e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0431\u043e\u043b\u044c\u043d\u0438\u0447\u043d\u043e\u0433\u043e \u043b\u0438\u0441\u0442\u0430 (\u0442\u043e\u043b\u044c\u043a\u043e \u0434\u043b\u044f \u0431\u043e\u043b\u044c\u043d\u0438\u0447\u043d\u043e\u0433\u043e)", None))
        self.combo_type.setItemText(0, QCoreApplication.translate("Form", u"\u041e\u043f\u043b\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u044b\u0439 \u043e\u0442\u043f\u0443\u0441\u043a", None))
        self.combo_type.setItemText(1, QCoreApplication.translate("Form", u"\u041d\u0435 \u043e\u043f\u043b\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u044b\u0439 \u043e\u0442\u043f\u0443\u0441\u043a", None))
        self.combo_type.setItemText(2, QCoreApplication.translate("Form", u"\u0411\u043e\u043b\u044c\u043d\u0438\u0447\u043d\u044b\u0439 \u043b\u0438\u0441\u0442", None))

        self.btn_save.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

