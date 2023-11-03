import pytest
from starlette.testclient import TestClient

from tests.sample_app import app


@pytest.fixture
def client():
    return TestClient(app)
