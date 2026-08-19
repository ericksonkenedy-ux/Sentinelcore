from fastapi import FastAPI
from backend.app.api import auth, assets, events, alerts, incidents

app = FastAPI(title="Sentinelcore")

# Include routers
app.include_router(auth.router, prefix="/auth")
app.include_router(assets.router, prefix="/assets")
app.include_router(events.router, prefix="/events")
app.include_router(alerts.router, prefix="/alerts")
app.include_router(incidents.router, prefix="/incidents")

@app.get("/")
def read_root():
    return {"ok": True, "service": "Sentinelcore backend"}
