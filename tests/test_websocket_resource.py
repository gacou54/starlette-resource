import pytest


@pytest.mark.parametrize('name, expected', [
    ('Gabriel', 'Hello Gabriel!'),
    ('John', 'Hello John!'),
])
def test_websocket_resource(client, name, expected) -> None:
    with client.websocket_connect('/websocket_greet') as websocket:
        websocket.send_text(name)
        result = websocket.receive_text()

        assert result == expected
