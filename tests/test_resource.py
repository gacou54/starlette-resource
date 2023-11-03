import pytest


@pytest.mark.parametrize('name, expected', [
    ('Gabriel', 'Hello Gabriel!'),
    ('John', 'Hello John!'),
])
def test_resource(client, name, expected) -> None:
    response = client.get(f'/greet/{name}')

    assert response.text == expected
