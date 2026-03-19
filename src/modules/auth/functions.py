from fastapi import status
from fastapi.responses import JSONResponse


# User Function to Handle User Login POST Request
async def user_login_post() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"success": True, "message": "Login successful"},
    )
