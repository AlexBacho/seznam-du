from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from . import tasks
from ..core import constants

router = APIRouter()
templates = Jinja2Templates(directory=constants.TEMPLATE_DIR)


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    movies = tasks.get_movie_list()
    return templates.TemplateResponse(constants.TEMPLATE_PATH, {"request": request, "movies": movies})
