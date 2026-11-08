# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addworker.ui'
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
        Form.resize(723, 557)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label)

        self.line_last = QLineEdit(Form)
        self.line_last.setObjectName(u"line_last")

        self.verticalLayout.addWidget(self.line_last)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_2)

        self.line_first = QLineEdit(Form)
        self.line_first.setObjectName(u"line_first")

        self.verticalLayout.addWidget(self.line_first)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_3)

        self.line_middle = QLineEdit(Form)
        self.line_middle.setObjectName(u"line_middle")

        self.verticalLayout.addWidget(self.line_middle)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_5)

        self.line_date = QLineEdit(Form)
        self.line_date.setObjectName(u"line_date")

        self.verticalLayout.addWidget(self.line_date)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_4)

        self.line_passport = QLineEdit(Form)
        self.line_passport.setObjectName(u"line_passport")

        self.verticalLayout.addWidget(self.line_passport)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_6)

        self.line_birth = QLineEdit(Form)
        self.line_birth.setObjectName(u"line_birth")

        self.verticalLayout.addWidget(self.line_birth)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_7)

        self.line_inn = QLineEdit(Form)
        self.line_inn.setObjectName(u"line_inn")

        self.verticalLayout.addWidget(self.line_inn)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_8)

        self.line_snils = QLineEdit(Form)
        self.line_snils.setObjectName(u"line_snils")

        self.verticalLayout.addWidget(self.line_snils)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_9)

        self.combo_position = QComboBox(Form)
        self.combo_position.setObjectName(u"combo_position")

        self.verticalLayout.addWidget(self.combo_position)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.label_10)

        self.combo_department = QComboBox(Form)
        self.combo_department.setObjectName(u"combo_department")

        self.verticalLayout.addWidget(self.combo_department)

        self.combo_gender = QComboBox(Form)
        self.combo_gender.addItem("")
        self.combo_gender.addItem("")
        self.combo_gender.setObjectName(u"combo_gender")

        self.verticalLayout.addWidget(self.combo_gender)

        self.btn_save = QPushButton(Form)
        self.btn_save.setObjectName(u"btn_save")

        self.verticalLayout.addWidget(self.btn_save)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0435\u043c\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0418\u041d\u041d", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0421\u041d\u0418\u041b\u0421", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0434\u0435\u043b", None))
        self.combo_gender.setItemText(0, QCoreApplication.translate("Form", u"M", None))
        self.combo_gender.setItemText(1, QCoreApplication.translate("Form", u"F", None))

        self.btn_save.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u043d\u044f\u0442\u044c", None))
    # retranslateUi

