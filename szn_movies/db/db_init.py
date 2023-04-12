from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..core import constants
from .models import BaseModel

engine = create_engine(constants.DB_NAME)


def init_db():
    BaseModel.metadata.create_all(engine)


def get_session_maker():
    return sessionmaker(engine)
