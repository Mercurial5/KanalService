from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from os import getenv

engine = create_engine(getenv('DATABASE_URI'), future=True)
Base = declarative_base()

from models.Orders import Orders

Base.metadata.create_all(engine)
