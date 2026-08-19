from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, status

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = None):
    # Placeholder: validate token and return user
    if credentials is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    token = credentials.credentials
    if token != "dev-token":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")
    return {"username": "dev"}
