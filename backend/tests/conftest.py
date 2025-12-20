import pytest

from db.test_session import TestingSessionLocal, create_test_db, drop_test_db


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    create_test_db()
    yield
    drop_test_db()


@pytest.fixture
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
