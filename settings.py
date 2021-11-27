from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

sqlite_engine = create_engine("sqlite:///renne.db?check_same_thread=False&echo=True")

Base = declarative_base()
