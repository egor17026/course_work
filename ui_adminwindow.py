# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(931, 696)
        self.verticalLayout = QVBoxLayout(AdminWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(AdminWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-20, 10, 886, 335))
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Confirm = QPushButton(self.tab)
        self.Confirm.setObjectName(u"Confirm")
        self.Confirm.setGeometry(QRect(680, 360, 181, 36))
        self.btn_logout = QPushButton(self.tab)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setGeometry(QRect(750, 600, 151, 36))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.tab_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_approve_hire = QPushButton(self.widget_2)
        self.btn_approve_hire.setObjectName(u"btn_approve_hire")

        self.verticalLayout_3.addWidget(self.btn_approve_hire)

        self.btn_approve_fire = QPushButton(self.widget_2)
        self.btn_approve_fire.setObjectName(u"btn_approve_fire")

        self.verticalLayout_3.addWidget(self.btn_approve_fire)

        self.table_workers = QTableWidget(self.widget_2)
        self.table_workers.setObjectName(u"table_workers")

        self.verticalLayout_3.addWidget(self.table_workers)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.widget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget_2 = QTabWidget(self.tab_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_5.addWidget(self.label)

        self.line_pos_name = QLineEdit(self.tab_4)
        self.line_pos_name.setObjectName(u"line_pos_name")

        self.verticalLayout_5.addWidget(self.line_pos_name)

        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_5.addWidget(self.label_2)

        self.line_oklad = QLineEdit(self.tab_4)
        self.line_oklad.setObjectName(u"line_oklad")

        self.verticalLayout_5.addWidget(self.line_oklad)

        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_5.addWidget(self.label_3)

        self.line_rate = QLineEdit(self.tab_4)
        self.line_rate.setObjectName(u"line_rate")

        self.verticalLayout_5.addWidget(self.line_rate)

        self.btn_add_pos = QPushButton(self.tab_4)
        self.btn_add_pos.setObjectName(u"btn_add_pos")

        self.verticalLayout_5.addWidget(self.btn_add_pos)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_6 = QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.line_2 = QFrame(self.tab_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_2)

        self.label_4 = QLabel(self.tab_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_6.addWidget(self.label_4)

        self.line_dept_name = QLineEdit(self.tab_5)
        self.line_dept_name.setObjectName(u"line_dept_name")

        self.verticalLayout_6.addWidget(self.line_dept_name)

        self.btn_add_dept = QPushButton(self.tab_5)
        self.btn_add_dept.setObjectName(u"btn_add_dept")

        self.verticalLayout_6.addWidget(self.btn_add_dept)

        self.line = QFrame(self.tab_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.tabWidget_2.addTab(self.tab_5, "")

        self.verticalLayout_4.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(AdminWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminWindow", u"ID", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.Confirm.setText(QCoreApplication.translate("AdminWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.btn_logout.setText(QCoreApplication.translate("AdminWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AdminWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.btn_approve_hire.setText(QCoreApplication.translate("AdminWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.btn_approve_fire.setText(QCoreApplication.translate("AdminWindow", u"\u0423\u0432\u043e\u043b\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AdminWindow", u"\u041a\u0430\u0434\u0440\u043e\u0432\u044b\u0435 \u043f\u0440\u0438\u043a\u0430\u0437\u044b", None))
        self.label.setText(QCoreApplication.translate("AdminWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("AdminWindow", u"\u041e\u043a\u043b\u0430\u0434", None))
        self.label_3.setText(QCoreApplication.translate("AdminWindow", u"\u0421\u0442\u0430\u0432\u043a\u0430(\u043f\u043e\u0447\u0430\u0441\u043e\u0432\u0430\u044f)", None))
        self.btn_add_pos.setText(QCoreApplication.translate("AdminWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("AdminWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("AdminWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043e\u0442\u0434\u0435\u043b\u0430", None))
        self.btn_add_dept.setText(QCoreApplication.translate("AdminWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0434\u0435\u043b", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("AdminWindow", u"\u041e\u0442\u0434\u0435\u043b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("AdminWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438", None))
    # retranslateUi

