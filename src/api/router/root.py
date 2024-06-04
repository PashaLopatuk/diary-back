from fastapi import FastAPI, APIRouter

from src.api.router.auth import auth_router


def init_routers(app: FastAPI) -> None:
    root_router = APIRouter(prefix="/api/v1/diary")

    root_router.include_router(auth_router)

    app.include_router(root_router)
    return app
