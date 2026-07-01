import sqlite3

DATABASE = "scanner.db"

def init_db():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        url TEXT,

        ip TEXT,

        status INTEGER,

        response_time REAL,

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

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
    INSERT INTO scans
    (
        timestamp,
        url,
        ip,
        status,
        response_time,
        risk,
        score
    )

    VALUES (?,?,?,?,?,?,?)

    """,

    (

        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        report.get("url",""),

        report.get("ip",""),

        report.get("status",0),

        report.get("response_time",0),

        report.get("risk","Unknown"),

        report.get("score",0)

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