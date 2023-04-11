import uvicorn

from szn_movies.app import app
from szn_movies.db import init_db


def main():
    init_db()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
