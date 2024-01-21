import uvicorn
from fastapi import FastAPI

from app.api.meeting_room import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_title,
    description='Room reservation API: An asynchronous application for '
                'efficient office space booking.',
)

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
