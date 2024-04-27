import pytest

# Тестовый пользователь
@pytest.fixture()
async def create_user(client):
    user = {
        "item": {
            "name": "Иван",
            "surname": "Иванов"
        }
    }
    response = await client.post("/api/users/", json=user)
    new_user_id = response.json()['id']
    return new_user_id