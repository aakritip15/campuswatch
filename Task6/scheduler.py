import schedule
import time
from db import init_db
from health_fetcher import fetch_camera_health

if __name__ == "__main__":
    init_db()
    print("Database initialized. Starting health data scheduler...")

    schedule.every(30).seconds.do(fetch_camera_health)

    while True:
        schedule.run_pending()
        time.sleep(1)
