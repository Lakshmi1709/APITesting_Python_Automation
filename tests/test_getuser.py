import pytest
from utilities.apis import APIS
import uuid

@pytest.fixture(scope='module')
def api_client():
    return APIS()

# To retrieve data
def test_getuser_validation(api_client):
    response = api_client.get('users')
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

# To crate users
def test_create_user(api_client, load_user_data):
    # user_data = {
    #     "name":"sai",
    #     "username":"QA User",
    #     "email":"test124@email.com"
    # }

    user_data = load_user_data['new_user']

# To create new email everytime
    unique_email = f'{uuid.uuid4().hex[:8]}@gmail.com'
    print(unique_email)
    user_data['email'] = unique_email

    response = api_client.post('users', user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == "sai"


    responseget = api_client.get('users/10')
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()['name'] == 'Clementina DuBuque'

# Update data
def test_update_user(api_client):
    user_data = {
        "name":"sailakshmi",
        "username":"QA Tester",
        "email":"tes09874@email.com"
    }
    response = api_client.put('users/1', user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == "sailakshmi"

# Delete Data
def test_delete_user(api_client):
    response = api_client.delete('users/1')
    print(response.json())
    assert response.status_code == 200
