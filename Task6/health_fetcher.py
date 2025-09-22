import random
from datetime import datetime, timezone
from db import insert_camera_health

def fetch_camera_health():
    """
    Simulates fetching health data from multiple cameras.
    Returns the list of camera health objects fetched.
    """
    camera_ids = ["CAM-01", "CAM-02", "CAM-03"]
    statuses = ["OK", "WARNING", "OFFLINE"]

    results = []
    for camera_id in camera_ids:
        status = random.choice(statuses)
        temperature = round(random.uniform(35.0, 65.0), 2)
        last_heartbeat = datetime.now(timezone.utc).isoformat()

        print(f"[INFO] Camera {camera_id}: status={status}, temp={temperature}, heartbeat={last_heartbeat}")
        
        insert_camera_health(camera_id, status, temperature, last_heartbeat)

        results.append({
            "camera_id": camera_id,
            "status": status,
            "temperature": temperature,
            "last_heartbeat": last_heartbeat
        })
    return results
