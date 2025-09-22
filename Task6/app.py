from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from db import init_db
from health_fetcher import fetch_camera_health

app = FastAPI(title="Camera Health API", version="1.0", lifespan="lifespan")
 
@asynccontextmanager
async def lifespan(app: FastAPI): 
    init_db()
    print("Database initialized on app startup.")
    yield 
    print("Application is shutting down.")

app = FastAPI(
    title="Camera Health API", 
    version="1.0", 
    lifespan=lifespan  
)

@app.get("/")
def home():
    return {"message": "Camera Health API is running!"}

@app.get("/health/fetch")
def fetch_health_data():
    results = fetch_camera_health()
    return {"status": "success", "records_fetched": len(results), "data": results}
