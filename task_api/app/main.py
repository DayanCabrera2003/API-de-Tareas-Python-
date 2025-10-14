from .routers import tasks
from fastapi import FastAPI
from .routers.tasks import router as tasks_router


app = FastAPI(title="Task API")
app.include_router(tasks_router)