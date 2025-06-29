# Routes, Define your routes here
from auth.functions import user_login
from fastapi import APIRouter

# Router
auth_router = APIRouter()


# Route to Handle User Login
@auth_router.post("/login")
async def user_login_post_call():
    """
    Handles user login.

    Returns:
        JSONResponse: A JSON response indicating the login status.
    """
    return user_login()
