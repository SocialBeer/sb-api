from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .config import config

Base = declarative_base()

engine = create_engine(
    config.db_url,
)

Session = sessionmaker(
    engine,
)


def get_session() -> Session:
    session = Session()
    
    try:
        yield session
    except Exception as e:
        print(e)
    finally:
        session.close()


