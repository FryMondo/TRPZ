from database import get_connection

class ConfigOptionsRepository:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def add(self, create_shortcut, install_directory):
        sql = "INSERT INTO ConfigOptions (create_shortcut, install_directory) VALUES (%s, %s)"
        values = (create_shortcut, install_directory)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, config_id):
        sql = "SELECT * FROM ConfigOptions WHERE config_id = %s"
        self.cursor.execute(sql, (config_id,))
        return self.cursor.fetchone()


class FilesRepository:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def add(self, file_name, file_path, file_type, file_size):
        sql = "INSERT INTO Files (file_name, file_path, file_type, file_size) VALUES (%s, %s, %s, %s)"
        values = (file_name, file_path, file_type, file_size)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, file_id):
        sql = "SELECT * FROM Files WHERE file_id = %s"
        self.cursor.execute(sql, (file_id,))
        return self.cursor.fetchone()


class InstallationsRepository:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def add(self, install_date, config_id, file_id):
        sql = "INSERT INTO Installations (install_date, config_id, file_id) VALUES (%s, %s, %s)"
        values = (install_date, config_id, file_id)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get(self, installation_id):
        sql = "SELECT * FROM Installations WHERE installation_id = %s"
        self.cursor.execute(sql, (installation_id,))
        return self.cursor.fetchone()
