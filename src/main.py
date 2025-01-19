from fastapi import FastAPI
from routes.root import router as root_router

app = FastAPI()

# Include the routers defined in your route files
app.include_router(root_router)
