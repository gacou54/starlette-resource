from starlette.testclient import TestClient

from tests.sample_app import app

client = TestClient(app)


def test_resource() -> None:
    expected_message = 'Hello John!'

    response = client.get('/greet/John')

    assert response.text == expected_message
