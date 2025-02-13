import pytest
from myapp.models import init_db, Session


@pytest.fixture(scope="function")
def db_session():
    init_db()

    session = Session()
    yield session

    session.close()
