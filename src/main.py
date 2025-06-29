from fastapi import FastAPI

from routes.v1 import v1_router

app = FastAPI()

# Include the routers defined in your route files
app.include_router(v1_router, prefix="/api/v1")
