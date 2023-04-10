from aiohttp import ClientSession
from asyncio import sleep

from ..core import constants
from ..db import ops as db


def get_movie_list():
    return


async def update_movie_list():
    while True:
        async with ClientSession() as s:
            async with s.get(constants.MOVIE_LIST_URL) as resp:
                movies = await resp.text()
                db.update_movie_list(movies)
        await sleep(constants.MOVIE_UPDATE_PERIOD)
