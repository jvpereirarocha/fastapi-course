from http import HTTPStatus


def test_successfull_user_creation(client, mock_user_schema, mock_user_public):
    user_data = {**mock_user_schema}
    response = client.post('/api/v1/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED  # 201 - CREATED
    user_public = mock_user_public(user_schema=mock_user_schema)
    assert response.json() == {
        **user_public,
        'id': 1,
    }


def test_get_all_users(client, mock_user_schema, mock_user_public):
    response = client.get('/api/v1/users/')
    user_public = mock_user_public(mock_user_schema)
    user_public['id'] = 1
    assert response.json() == {'users': [user_public]}
