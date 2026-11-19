# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AccWindow(object):
    def setupUi(self, AccWindow):
        if not AccWindow.objectName():
            AccWindow.setObjectName(u"AccWindow")
        AccWindow.resize(936, 549)
        self.verticalLayout = QVBoxLayout(AccWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(AccWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_workers = QTableWidget(self.tab)
        if (self.table_workers.columnCount() < 4):
            self.table_workers.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_workers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_workers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_workers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_workers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_workers.setObjectName(u"table_workers")

        self.verticalLayout_2.addWidget(self.table_workers)

        self.btn_calc = QPushButton(self.tab)
        self.btn_calc.setObjectName(u"btn_calc")

        self.verticalLayout_2.addWidget(self.btn_calc)

        self.btn_logout = QPushButton(self.tab)
        self.btn_logout.setObjectName(u"btn_logout")

        self.verticalLayout_2.addWidget(self.btn_logout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.table_payroll = QTableWidget(self.tab_2)
        self.table_payroll.setObjectName(u"table_payroll")

        self.verticalLayout_3.addWidget(self.table_payroll)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(AccWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AccWindow)
    # setupUi

    def retranslateUi(self, AccWindow):
        AccWindow.setWindowTitle(QCoreApplication.translate("AccWindow", u"AccWindow", None))
        ___qtablewidgetitem = self.table_workers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AccWindow", u"ID", None))
        ___qtablewidgetitem1 = self.table_workers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AccWindow", u"\u0424\u0418\u041e", None))
        ___qtablewidgetitem2 = self.table_workers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AccWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        ___qtablewidgetitem3 = self.table_workers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AccWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.btn_calc.setText(QCoreApplication.translate("AccWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.btn_logout.setText(QCoreApplication.translate("AccWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AccWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AccWindow", u"\u0412\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u044c", None))
    # retranslateUi

