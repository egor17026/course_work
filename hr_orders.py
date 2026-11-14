from PySide6.QtWidgets import QWidget, QTableWidgetItem
from ui_hr_orders import Ui_Form
from SalaryDB import CreateDatasource

class HROrdersWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = CreateDatasource()
        self.load_vacations()
        self.load_sicks()

    def load_vacations(self):
        vacations = self.db.get_all_vacations()
        self.ui.table_vacations.setRowCount(len(vacations))
        # Настраиваем колонки (если не сделал в Дизайнере)
        self.ui.table_vacations.setColumnCount(7)
        self.ui.table_vacations.setHorizontalHeaderLabels(["ID", "Фамилия", "Имя", "Тип", "Начало", "Конец", "Дней"])

        for row_idx, vac in enumerate(vacations):
            for col_idx, value in enumerate(vac):
                self.ui.table_vacations.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def load_sicks(self):
        sicks = self.db.get_all_sick_leaves()
        self.ui.table_sicks.setRowCount(len(sicks))
        self.ui.table_sicks.setColumnCount(7)
        self.ui.table_sicks.setHorizontalHeaderLabels(["ID", "Фамилия", "Имя", "Начало", "Конец", "Дней", "Номер листа"])

        for row_idx, sick in enumerate(sicks):
            for col_idx, value in enumerate(sick):
                self.ui.table_sicks.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
