from starlette.testclient import TestClient

from tests.sample_app import app

client = TestClient(app)


def test_websocket_resource() -> None:
    expected_message = 'Hello John!'

    with client.websocket_connect('/websocket_greet') as websocket:
        websocket.send_text('John')
        result = websocket.receive_text()

        assert result == expected_message
