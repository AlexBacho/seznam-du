from asyncio import get_event_loop
from fastapi import FastAPI

from .api.router import router
from .api.tasks import update_movie_list

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def schedule_periodic():
    loop = get_event_loop()
    loop.create_task(update_movie_list())
