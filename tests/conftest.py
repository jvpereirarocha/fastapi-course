import pytest
from fastapi.testclient import TestClient

from fast_course.main import app


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
