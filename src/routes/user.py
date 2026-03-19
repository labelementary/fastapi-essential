from fastapi import APIRouter

from src.modules.auth.routes import auth_router

# Configured Router for User Routes
root_user_router = APIRouter(prefix="/user")

# Include User Auth Routers
root_user_router.include_router(auth_router, tags=["User Auth Routes"])
