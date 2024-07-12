from http import HTTPStatus


def test_root_should_return_ok_and_hello_world(mock_client):
    client = mock_client
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK  # 200 - OK
    assert response.json() == {'message': 'Hello, world!'}
