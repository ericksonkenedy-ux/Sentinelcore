from fastapi import APIRouter
from backend.app.schemas.incidents import IncidentCreate

router = APIRouter()

@router.post("/")
def create_incident(incident: IncidentCreate):
    return {"id": 1, **incident.dict()}
