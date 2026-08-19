from fastapi import APIRouter, Depends
from backend.app.core.security import get_current_user

router = APIRouter()

@router.post("/login")
def login():
    return {"access_token": "dev-token", "token_type": "bearer"}

@router.get("/me")
def me(user=Depends(get_current_user)):
    return user
