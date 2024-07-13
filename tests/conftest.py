import pytest
from fastapi.testclient import TestClient

from fast_course.main import app


@pytest.fixture
def client():
    return TestClient(app)
