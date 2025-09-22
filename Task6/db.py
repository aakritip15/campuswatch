import sqlite3

DB_NAME = "camera_health.db"

def init_db(): 
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS camera_health (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            camera_id TEXT NOT NULL,
            status TEXT NOT NULL,
            temperature REAL,
            last_heartbeat TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_camera_health(camera_id, status, temperature, last_heartbeat): 
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO camera_health (camera_id, status, temperature, last_heartbeat)
        VALUES (?, ?, ?, ?)
    """, (camera_id, status, temperature, last_heartbeat))
    conn.commit()
    conn.close()
