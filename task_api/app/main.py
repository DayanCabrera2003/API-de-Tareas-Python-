from .routers import router
from fastapi import FastAPI
from .routers.router import router as tasks_router


app = FastAPI(title="Task API")
app.include_router(tasks_router)