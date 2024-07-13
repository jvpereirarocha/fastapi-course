from http import HTTPStatus


def test_successfull_user_creation(mock_client):
    client = mock_client
    user_data = {'username': 'test', 'email': 'test@gmail.com', 'password': 'test@123'}
    response = client.post('/api/v1/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED  # 201 - CREATED
    del user_data['password']  # Throwing away the password. We won't need it
    assert response.json() == {
        **user_data,
        'id': 1,
    }
