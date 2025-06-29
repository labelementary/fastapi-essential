from fastapi import APIRouter

from modules.auth.routes import auth_router

v1_router = APIRouter()

v1_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
