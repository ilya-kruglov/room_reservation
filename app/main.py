from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_title,
    description='Room reservation API: An asynchronous application for '
                'efficient office space booking.',
)

app.include_router(main_router)
