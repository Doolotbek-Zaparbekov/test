import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS books(
                    id INTEGER PRIMARY KEY,
                    book TEXT NOT NULL,
                    rating TEXT,
                    reading TEXT INTEGER
                    )
        """)
            
    def add_book(self, book: str, rating: int, reading: int):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                INSERT INTO books (book, rating, reading) VALUES (?, ?, ?)
                """,
                (book, bool(rating), int(reading))
            )
            conn.commit()
