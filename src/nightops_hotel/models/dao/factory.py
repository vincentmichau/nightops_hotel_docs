from pathlib import Path
import sqlite3

class SQLiteDaoFactory:
    """Factory DAO SQLite locale : unique point d'entrée stockage."""
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self):
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        return connection
