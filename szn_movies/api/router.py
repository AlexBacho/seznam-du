from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from . import tasks
from ..core import constants

router = APIRouter()
templates = Jinja2Templates(directory=constants.TEMPLATE_DIR)


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request, name_filter="", desc_toggle=False):
    movies = tasks.get_movie_list(name_filter, desc_toggle)
    return templates.TemplateResponse(constants.TEMPLATE_PATH, {
        "request": request,
        "movies": movies,
        "name_filter": name_filter,
        "desc_toggle": desc_toggle
    })
