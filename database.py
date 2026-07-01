import sqlite3

DATABASE = "scanner.db"

def init_db():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        url TEXT,

        ip TEXT,

        status INTEGER,

        risk TEXT,

        score INTEGER

    )
    """)

    conn.commit()

    conn.close()


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS scans(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            url TEXT,

            ip TEXT,

            status INTEGER,

            score INTEGER,

            risk TEXT,

            response_time REAL,

            scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)

    conn.commit()

    conn.close()

def save_scan(report):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO scans(

            url,

            ip,

            status,

            score,

            risk,

            response_time

        )

        VALUES(?,?,?,?,?,?)

    """,(

        report["url"],

        report["ip"],

        report["status"],

        report["score"],

        report["risk"],

        report["response_time"]

    ))

    conn.commit()

    conn.close()

def get_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM scans

        ORDER BY scan_date DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

if __name__ == "__main__":
    init_db()