from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="SIEMLite",
    description="Mini SIEM uygulaması - Giriş/Orta Seviye",
    version="0.1.0"
)

# ----- MODELS -----
class LogEntry(BaseModel):
    timestamp: datetime
    source_ip: str
    event_type: str
    severity: Optional[str] = "info"
    message: str
    user: Optional[str] = None

# In-memory store for simplicity
log_store: List[LogEntry] = []

# ----- ROUTES -----

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "SIEMLite Backend"}

@app.post("/api/logs/ingest", tags=["Logs"])
def ingest_log(entry: LogEntry):
    log_store.append(entry)
    return {"message": "Log stored", "count": len(log_store)}

@app.get("/api/logs", response_model=List[LogEntry], tags=["Logs"])
def get_logs(
    source_ip: Optional[str] = Query(None),
    event_type: Optional[str] = Query(None),
    severity: Optional[str] = Query(None)
):
    results = log_store
    if source_ip:
        results = [log for log in results if log.source_ip == source_ip]
    if event_type:
        results = [log for log in results if log.event_type == event_type]
    if severity:
        results = [log for log in results if log.severity == severity]
    return results
