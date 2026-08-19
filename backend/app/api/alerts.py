from fastapi import APIRouter
from backend.app.schemas.alerts import AlertCreate

router = APIRouter()

@router.post("/")
def create_alert(alert: AlertCreate):
    return {"id": 1, **alert.dict()}
