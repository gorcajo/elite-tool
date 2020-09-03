import os.path
import subprocess
from typing import List

import sqlite3


DB_FILE = "database.db"


class DataBase():

    def __init__(self):
        pass

    def find_all(self):
        pass

    def insert(self, repairment: dict):
        pass

    def update(self, id: int, repairment: dict):
        pass

    def delete(self, id: int):
        pass


class SqliteDataBase(DataBase):

    def __init__(self):
        if not os.path.isfile(DB_FILE):
            subprocess.run([
                "sqlite3",
                DB_FILE,
                """CREATE TABLE IF NOT EXISTS repairments(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    customer_name TEXT,
                    customer_phone TEXT,
                    type TEXT,
                    manufacturer TEXT,
                    model TEXT,
                    serial_number TEXT,
                    reception_date TEXT,
                    estimated_cost INTEGER,
                    description TEXT
                )"""])


    def find_all(self) -> List[dict]:
        with sqlite3.connect(DB_FILE) as conn:
            conn.row_factory = sqlite3.Row

            qry = "SELECT * FROM repairments"
            rows = conn.cursor().execute(qry, []).fetchall()

            if len(rows) == 0:
                return None
            else:
                repairments = []

                for row in rows:
                    repairments.append({
                        "id": row["id"],
                        "customer_name": row["customer_name"],
                        "customer_phone": row["customer_phone"],
                        "type": row["type"],
                        "manufacturer": row["manufacturer"],
                        "model": row["model"],
                        "serial_number": row["serial_number"],
                        "reception_date": row["reception_date"],
                        "estimated_cost": row["estimated_cost"],
                        "description": row["description"],
                    })
                
                return repairments


    def find_by_id(self, id: int) -> dict:
        with sqlite3.connect(DB_FILE) as conn:
            conn.row_factory = sqlite3.Row

            qry = "SELECT * FROM repairments WHERE id = ?"
            rows = conn.cursor().execute(qry, [id]).fetchall()

            if len(rows) == 0:
                return None

            elif len(rows) == 1:
                row = rows[0]

                return {
                    "id": row["id"],
                    "customer_name": row["customer_name"],
                    "customer_phone": row["customer_phone"],
                    "type": row["type"],
                    "manufacturer": row["manufacturer"],
                    "model": row["model"],
                    "serial_number": row["serial_number"],
                    "reception_date": row["reception_date"],
                    "estimated_cost": row["estimated_cost"],
                    "description": row["description"],
                }

            else:
                raise ValueError()


    def insert(self, repairment: dict) -> int:
        with sqlite3.connect(DB_FILE) as conn:
            conn.row_factory = sqlite3.Row

            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO repairments(
                    customer_name,
                    customer_phone,
                    type,
                    manufacturer,
                    model,
                    serial_number,
                    reception_date,
                    estimated_cost,
                    description)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                [
                    repairment["customer_name"],
                    repairment["customer_phone"],
                    repairment["type"],
                    repairment["manufacturer"],
                    repairment["model"],
                    repairment["serial_number"],
                    repairment["reception_date"],
                    repairment["estimated_cost"],
                    repairment["description"],
                ]
            )
            
            return cursor.lastrowid


    def update(self, id: int, repairment: dict):
        with sqlite3.connect(DB_FILE) as conn:
            conn.row_factory = sqlite3.Row

            conn.cursor().execute(
                """UPDATE repairments SET
                    customer_name = ?,
                    customer_phone = ?,
                    type = ?,
                    manufacturer = ?,
                    model = ?,
                    serial_number = ?,
                    reception_date = ?,
                    estimated_cost = ?,
                    description = ?
                    WHERE id = ?""",
                [
                    repairment["customer_name"],
                    repairment["customer_phone"],
                    repairment["type"],
                    repairment["manufacturer"],
                    repairment["model"],
                    repairment["serial_number"],
                    repairment["reception_date"],
                    repairment["estimated_cost"],
                    repairment["description"],
                    id,
                ]
            )


    def delete(self, id: int):
        with sqlite3.connect(DB_FILE) as conn:
            conn.row_factory = sqlite3.Row
            conn.cursor().execute("DELETE FROM repairments WHERE id = ?", [id])
