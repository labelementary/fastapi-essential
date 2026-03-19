from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.user import root_user_router

# Configure FastAPI Application
app = FastAPI(
    title="FastAPI Essential",
    description="FastAPI Essential, Pre-Configured FastAPI Project with all essential dependencies and configurations for a robust and scalable FastAPI application.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


# Root Route
@app.get("/")
async def root():
    return {"message": "Welcome to ShareToCare, Please Visit sharetocarefoundation.in"}


# Include the routers defined in your route files
app.include_router(root_user_router, prefix="/api/v1")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=[
        # Local Routes
        "http://localhost:7070",
        "http://127.0.0.1:7070",
        "https://127.0.0.1:7070",
        "https://localhost:7070",
        # Development Routes
        # Production Routes
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
