from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

import app.db.base_registry # type: ignore


TEST_DATABASE_URL = "sqlite+pysqlite:///:memory:"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

def create_test_db():
    Base.metadata.create_all(bind=engine)

def drop_test_db():
    Base.metadata.drop_all(bind=engine)
