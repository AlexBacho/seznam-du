from pathlib import Path

MOVIE_LIST_URL = "https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json"
MOVIE_UPDATE_PERIOD = 60
DB_NAME = "sqlite:///local.db"
TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"
TEMPLATE_PATH = "homepage.j2"