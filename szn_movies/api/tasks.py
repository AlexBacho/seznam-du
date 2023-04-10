import requests

from ..core.constants import MOVIE_LIST_URL


def get_movie_list():
    current_movie_list = fetch_movie_list_from_web()
    return current_movie_list


def fetch_movie_list_from_web():
    resp = requests.get(MOVIE_LIST_URL)
    return resp.json()
