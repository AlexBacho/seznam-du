import json

from aiohttp import ClientSession
from asyncio import sleep

from ..core import constants
from ..db import ops as db


def get_movie_list():
    # gets the movie list from db and cleans it up a bit for UI,
    # by splitting the main info from the rest
    ret = []
    movies = db.get_movies()
    for movie in movies:
        movie_data = {
            "name": movie["name"],
            "iconUri": movie["iconUri"],
        }
        extra_data = dict((k, v) for k, v in movie.items() if k not in movie_data)
        movie_data["extra_data"] = extra_data
        ret.append(movie_data)
    return ret


async def update_movie_list():
    while True:
        print("Scraping website for newest updates on movies.")
        async with ClientSession() as s:
            async with s.get(constants.MOVIE_LIST_URL) as resp:
                movies = await resp.text()
                db.update_movie_list(json.loads(movies))
        await sleep(constants.MOVIE_UPDATE_PERIOD)
