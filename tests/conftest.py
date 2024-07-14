import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_course.main import app
from fast_course.models.base import mapped_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def mock_user_schema():
    return {'username': 'test', 'email': 'test@gmail.com', 'password': 'test@123'}


@pytest.fixture
def mock_user_public():
    def _get_user_schema(user_schema: dict[str, str]) -> dict[str, str]:
        assert 'password' in user_schema
        del user_schema['password']
        return {**user_schema}

    return _get_user_schema


# Database configuration
@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    mapped_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    mapped_registry.metadata.drop_all(engine)
