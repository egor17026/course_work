from PySide6.QtWidgets import QWidget, QMessageBox
from ui_addworker import Ui_Form  # Импортируем дизайн (проверь название класса!)
from SalaryDB import CreateDatasource

class AddWorkerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.db = CreateDatasource()

        # Заполняем выпадающие списки при открытии окна
        self.load_combos()

        # Подключаем кнопку "Нанять"
        self.ui.btn_save.clicked.connect(self.save_worker)

    def load_combos(self):
        # Заполняем должности
        positions = self.db.get_all_positions()
        for pos_id, pos_name in positions:
            self.ui.combo_position.addItem(pos_name, pos_id)

        # Заполняем отделы
        departments = self.db.get_all_departments()
        for dep_id, dep_name in departments:
            self.ui.combo_department.addItem(dep_name, dep_id)

    def save_worker(self):
        # Берем данные из полей
        last_name = self.ui.line_last.text()
        first_name = self.ui.line_first.text()
        middle_name = self.ui.line_middle.text()
        birth_date = self.ui.line_birth.text()
        inn = self.ui.line_inn.text()
        snils = self.ui.line_snils.text()
        passport = self.ui.line_passport.text()
        gender = self.ui.combo_gender.currentText()
        hire_date = self.ui.line_date.text()

        # Берем ID из выпадающих списков
        position_id = self.ui.combo_position.currentData()
        department_id = self.ui.combo_department.currentData()

        # Проверка, что поля не пустые
        if not last_name or not first_name or not passport:
            QMessageBox.warning(self, "Ошибка", "Заполните обязательные поля (ФИО, паспорт)!")
            return

        # Отправляем в базу
        if self.db.hire_worker(
            last_name, first_name, middle_name,
            birth_date, inn, snils, passport, gender,
            position_id, department_id, hire_date
        ):
            QMessageBox.information(self, "Успех", "Работник добавлен!\nОжидайте подписи директора.")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось добавить работника.\nПроверьте формат даты (ГГГГ-ММ-ДД).")
