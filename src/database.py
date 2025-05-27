import sqlite3


class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact TEXT NOT NULL,
            number TEXT NOT NULL,
            additionally TEXT NOT NULL
        );
        """)
        self.conn.commit()

    def add_contact(self, contact, number, additionally):
        self.conn.execute("INSERT INTO contacts (contact, number, additionally) VALUES (?, ?, ?);", (contact, number, additionally))
        self.conn.commit()

    def delete_contact(self, id):
        self.conn.execute("DELETE FROM contacts WHERE id = ?;", (id,))
        self.conn.commit()

    def get_contact(self):
        return self.conn.execute("SELECT * FROM contacts;").fetchall()

    def clear_all(self):
        self.conn.execute("DELETE FROM contacts;")
        self.conn.commit()
