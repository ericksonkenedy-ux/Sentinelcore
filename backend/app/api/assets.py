from fastapi import APIRouter, Depends
from backend.app.schemas.assets import AssetCreate, Asset

router = APIRouter()

@router.get("/")
def list_assets():
    return []

@router.post("/")
def create_asset(asset: AssetCreate):
    return {"id": 1, **asset.dict()}
