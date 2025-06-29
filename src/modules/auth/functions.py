# Functions, Define your API functions here
from fastapi import status
from fastapi.responses import JSONResponse


# Function to Handle User Login
async def user_login() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"success": True, "message": "Login successful"},
    )
