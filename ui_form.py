# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(897, 258)
        Widget.setMaximumSize(QSize(1000, 258))
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 15))

        self.verticalLayout_2.addWidget(self.label)

        self.txt_login = QLineEdit(Widget)
        self.txt_login.setObjectName(u"txt_login")

        self.verticalLayout_2.addWidget(self.txt_login)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 15))

        self.verticalLayout_2.addWidget(self.label_2)

        self.txt_password = QLineEdit(Widget)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.txt_password)

        self.check = QPushButton(Widget)
        self.check.setObjectName(u"check")

        self.verticalLayout_2.addWidget(self.check)

        self.regist = QPushButton(Widget)
        self.regist.setObjectName(u"regist")
        self.regist.setEnabled(True)
        self.regist.setMinimumSize(QSize(150, 0))
        self.regist.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setUnderline(True)
        self.regist.setFont(font)
        self.regist.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.regist.setFlat(True)

        self.verticalLayout_2.addWidget(self.regist)

        self.checkBox = QCheckBox(Widget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.check.setText(QCoreApplication.translate("Widget", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.regist.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
    # retranslateUi

