from fastapi import APIRouter

from . import tasks

router = APIRouter()


@router.get("/")
async def read_root():
    return "homepage"


@router.get("/movies/")
async def get_movie_list():
    return tasks.get_movie_list()
