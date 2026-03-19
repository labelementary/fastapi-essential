from fastapi import APIRouter

from src.modules.auth.functions import user_login_post

# Configured Router for Authentication Routes for User
auth_router = APIRouter(prefix="/auth")


# Router Function to Handle User Login POST Request
@auth_router.post("/login")
async def user_login_post_call():
    return await user_login_post()
