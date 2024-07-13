from http import HTTPStatus


def test_user_creation(client, mock_user_schema, mock_user_public):
    user_data = {**mock_user_schema}
    response = client.post('/api/v1/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED  # 201
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


def test_fetch_one_user(client, mock_user_schema, mock_user_public):
    response = client.get('/api/v1/users/1')
    assert response.json() == {**mock_user_public(mock_user_schema), 'id': 1}


def test_user_update(client, mock_user_schema, mock_user_public):
    user_data = mock_user_schema
    response = client.post('/api/v1/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED  # 201

    # now, let's update the user
    new_email = 'mynewemail@gmail.com'
    user_data['email'] = new_email
    response = client.put('/api/v1/users/1', json=user_data)
    assert response.status_code == HTTPStatus.OK  # 200
    assert response.json() == {
        'username': user_data.get('username'),
        'email': new_email,
        'id': 1,
    }


def test_user_delete(client, mock_user_schema, mock_user_public):
    response = client.delete('/api/v1/users/1')
    assert response.status_code == HTTPStatus.NO_CONTENT  # 204
