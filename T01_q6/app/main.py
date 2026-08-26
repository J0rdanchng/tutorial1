from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import admin, users

app = FastAPI()

app.include_router(users.router)

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
)

# Serve static/index.html at the root
app.mount("/", StaticFiles(directory="static", html=True), name="static")
