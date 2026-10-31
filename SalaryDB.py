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

    def get_all_workers(self) -> list:
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT w.worker_id, w.last_name, w.first_name, p.position_name
                FROM workers w
                JOIN positions p ON w.position_id = p.position_id
            """)
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


_salary_db_instance = None

def CreateDatasource():
    global _salary_db_instance
    if _salary_db_instance is None:
        _salary_db_instance = SalaryDB()
    return _salary_db_instance
