import json

from .session import session
from .models import Movies

@session
def update_movie_list(s, movies):
    # If the data for each movie is static, deleting old
    # data would be redundant, but for our purposes, cleaning
    # up the table each time seems good enough. Also, there is no
    # information about the release date of the movies, or how long we want
    # to show them for, so I presume we'll always be showing all of them.
    s.query(Movies).delete()
    movies = [Movies(**m) for m in movies]
    s.add_all(movies)


@session
def get_movies(s):
    resp = s.query(Movies).all()
    return json.load(resp)
