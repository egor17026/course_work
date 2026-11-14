from PySide6.QtWidgets import QWidget
from ui_hr_menu import Ui_Form
from hr_window import HRWindow
from hr_orders import HROrdersWindow
from timesheet_window import TimesheetWindow

class HRMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.btn_workers.clicked.connect(self.open_workers)
        self.ui.btn_timesheet.clicked.connect(self.open_timesheet)
        self.ui.btn_orders.clicked.connect(self.open_orders)

    def open_workers(self):
        self.workers_win = HRWindow()
        self.workers_win.show()

    def open_timesheet(self):
        self.ts_win = TimesheetWindow()
        self.ts_win.show()

    def open_orders(self):
        self.orders_win = HROrdersWindow()
        self.orders_win.show()
