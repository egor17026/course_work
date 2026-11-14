from firebird.driver import connect, driver_config

class SalaryDB:
    def __init__(self):
        self.user = 'SYSDBA'
        self.password = 'masterkey'
        self.dbpath = 'localhost:/rdb/kyrsach.fdb'
        self.charset = 'UTF8'

        driver_config.server_defaults.user.value = self.user
        driver_config.server_defaults.password.value = self.password

    def get_connection(self):
        return connect(self.dbpath, charset=self.charset)

    def get_user(self, login: str):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT password_hash, is_active, role_id
                FROM users
                WHERE login = ?
            """, (login,))
            return cur.fetchone()
        finally:
            conn.close()

    def register_user(self, login: str, password: str, role_id: int):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT user_id FROM users WHERE login = ?", (login,))
            if cur.fetchone():
                print("Пользователь с таким логином уже существует")
                return False

            cur.execute("SELECT MAX(user_id) FROM users")
            max_id = cur.fetchone()[0]
            new_id = (max_id + 1) if max_id else 1

            cur.execute("""
                INSERT INTO users (user_id, login, password_hash, role_id, is_active, created_at)
                VALUES (?, ?, ?, ?, 0, CURRENT_TIMESTAMP)
                """, (new_id, login, password, role_id))

            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка регистрации: {e}")
            return False
        finally:
            conn.close()

    def get_all_workers(self) -> list:
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT w.worker_id, w.last_name, w.first_name, w.middle_name, p.position_name, d.department_name, w.status
                FROM workers w
                JOIN positions p ON w.position_id = p.position_id
                LEFT JOIN departments d ON w.department_id = d.department_id
            """)
            return cur.fetchall()
        finally:
            conn.close()

    def add_vacation(self, worker_id, date_start, date_end, vacation_type):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT DATEDIFF(DAY, ?, ?) + 1 FROM RDB$DATABASE", (date_start, date_end))
            days = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO vacations (vacation_id, worker_id, vacation_type, date_start, date_end, days_count)
                VALUES (NEXT VALUE FOR GEN_VACATIONS_ID, ?, ?, ?, ?, ?)
            """, (worker_id, vacation_type, date_start, date_end, days))
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка отпуска: {e}")
            return False
        finally:
            conn.close()

    def add_sick_leaves(self, worker_id, date_start, date_end, list_number):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT DATEDIFF(DAY, ?, ?) + 1 FROM RDB$DATABASE", (date_start, date_end))
            days = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO sick_leaves (sick_leave_id, worker_id, date_start, date_end, days_count, list_number)
                VALUES (NEXT VALUE FOR GEN_SICK_LEAVES_ID, ?, ?, ?, ?, ?)
            """, (worker_id, date_start, date_end, days, list_number))
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка больничного: {e}")
            return False
        finally:
            conn.close()

    def get_all_vacations(self):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT v.vacation_id, w.last_name, w.first_name, v.vacation_type, v.date_start, v.date_end, v.days_count
                FROM vacations v
                JOIN workers w ON v.worker_id = w.worker_id
            """)
            return cur.fetchall()
        finally:
            conn.close()

    def get_all_sick_leaves(self):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT s.sick_leave_id, w.last_name, w.first_name, s.date_start, s.date_end, s.days_count, s.list_number
                FROM sick_leaves s
                JOIN workers w ON s.worker_id = w.worker_id
            """)
            return cur.fetchall()
        finally:
            conn.close()

    def get_all_positions(self):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT position_id, position_name FROM positions")
            return cur.fetchall()
        finally:
            conn.close()

    def get_all_departments(self):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT department_id, department_name FROM departments")
            return cur.fetchall()
        finally:
            conn.close()

    def hire_worker(self, last_name, first_name, middle_name, birth_date, inn, snils, passport, gender, position_id, department_id, hire_date):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT MAX(worker_id) FROM workers")
            max_id = cur.fetchone()[0]
            new_id = (max_id + 1) if max_id else 1
            cur.execute("""
                INSERT INTO workers (
                    worker_id, last_name, first_name, middle_name,
                    birth_date, inn, snils, passport, gender,
                    position_id, department_id, hire_date, status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'на согласовании')
            """, (new_id, last_name, first_name, middle_name, birth_date,
                          inn, snils, passport, gender, position_id, department_id, hire_date))
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка найма: {e}")
            return False
        finally:
            conn.close()

    def get_all_users(self):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("SELECT user_id, login, is_active FROM users")
            return cur.fetchall()
        finally:
            conn.close()

    def activate_user(self, user_id: int):
        conn = self.get_connection()
        cur = conn.cursor()

        try:
            cur.execute("""UPDATE users
            SET is_active = 1
            WHERE user_id = ?
            """, (user_id,))
            conn.commit()
        finally:
            conn.close()

    def add_timesheet(self, worker_id, work_date, shift_type, hours_worked):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            # Ищем максимальный ID для новой записи
            cur.execute("SELECT MAX(timesheet_id) FROM timesheet")
            max_id = cur.fetchone()[0]
            new_id = (max_id + 1) if max_id else 1

            cur.execute("""
                INSERT INTO timesheet (timesheet_id, worker_id, work_date, shift_type, hours_worked)
                VALUES (?, ?, ?, ?, ?)
            """, (new_id, worker_id, work_date, shift_type, hours_worked))
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка табеля: {e}")
            return False
        finally:
            conn.close()

    def search_workers(self, text):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT w.worker_id, w.last_name, w.first_name, w.middle_name, p.position_name, d.department_name, w.status
                FROM workers w
                JOIN positions p ON w.position_id = p.position_id
                LEFT JOIN departments d ON w.department_id = d.department_id
                WHERE w.last_name LIKE ? OR w.first_name LIKE ?
            """, (f"%{text}%", f"%{text}%"))
            return cur.fetchall()
        finally:
            conn.close()

    def add_worker(self, last_name, first_name, position_id, hire_date):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO workers (last_name, first_name, position_id, hire_date, status)
                VALUES (?, ?, ?, ?, 'работает')
            """, (last_name, first_name, position_id, hire_date))
            conn.commit()
        finally:
            conn.close()

    def request_fire_worker(self, worker_id: int):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                UPDATE workers
                SET status = 'на увольнении'
                WHERE worker_id = ?
            """, (worker_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка запроса на увольнение: {e}")
            return False
        finally:
            conn.close()

    def approve_fire_worker(self, worker_id : int):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                UPDATE workers
                SET status = 'уволен', fire_date = CURRENT_DATE
                WHERE worker_id = ?
            """, (worker_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Ошибка подтверждения увольнения: {e}")
            return False
        finally:
            conn.close()

_salary_db_instance = None

def CreateDatasource():
    global _salary_db_instance
    if _salary_db_instance is None:
        _salary_db_instance = SalaryDB()
    return _salary_db_instance

