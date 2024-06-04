from fastapi import APIRouter


auth_router = APIRouter(prefix="/authentication", tags=["Authentication"])


@auth_router.get('/get_user/')
async def get_user() -> dict:
    return {"user": "User"}
