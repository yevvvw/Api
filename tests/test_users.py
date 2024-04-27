# Необходимые библиотеки
from fastapi import status
from utils import create_user
import asyncio

# Проверка получения списка пользвателей
# Код состояния - 404
async def test_get_users_http_404_not_found(client):
    detail = "Таблица пользователей пуста"
    response = await client.get("/api/users/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert detail == response.json()['message']
# Код состояния - 200
async def test_get_users(client, create_user):
    response = await client.get("/api/users/")
    assert response.status_code == status.HTTP_200_OK

# Проверка получения пользователя по id
# Код состояния - 200
async def test_get_user(client, create_user):
    user_id = create_user
    response = await client.get(f"/api/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    assert user_id == response.json()['id']
# Код состояния - 404
async def test_get_user_http_404_not_found(client):
    user_id = 0
    detail = "Пользователь не найден"
    response = await client.get(f"/api/users/{user_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert detail == response.json()['message']

# Проверка частичного обновления данных пользователя по id
# Код состояния - 200
async def test_patch_user(client, create_user):
    user_id = create_user
    new_surname = "Сидоров"

    user = {
        "item": {
            "surname": new_surname
        }
    }

    response = await client.patch(f"/api/users/{user_id}", json=user)
    assert response.status_code == status.HTTP_200_OK
    assert new_surname == response.json()['surname']
# Код состояния - 404
async def test_patch_user_http_404_not_found(client):
    user_id = 0
    detail = "Пользователь не найден"
    new_surname = "Сидоров"

    user = {
        "item": {
            "surname": new_surname
        }
    }

    response = await client.patch(f"/api/users/{user_id}", json=user)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert detail == response.json()['message']
# Код состояния - 422
async def test_patch_http_422(client):
    user_id = create_user
    new_name = 123

    user = {
        "item": {
            "name": new_name
        }
    }

    response = await client.patch(f"/api/users/{user_id}", json=user)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

# Проверка удаления пользователя по id
# Код состояния - 200
async def test_delete_user(client, create_user):
    user_id = create_user
    detail = f"Пользователь удалён {user_id}"
    response = await client.delete(f"/api/users/{user_id}")
    assert response.status_code == status.HTTP_200_OK
    assert detail == response.json()['message']
# Код состояния - 404
async def test_delete_user_http_404_not_found(client):
    user_id = 0
    detail = "Пользователь не найден"
    response = await client.delete(f"/api/users/{user_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert detail == response.json()['message']

# Проверка полного обновления данных пользвателя по id
# Код состояния - 200
async def test_update_user(client, create_user):
    user_id = create_user
    new_name = "Сергей"
    new_surname = "Смирнов"

    user = {
        "item": {
            "name": new_name,
            "surname": new_surname
        }
    }

    response = await client.put(f"/api/users/{user_id}", json=user)
    assert response.status_code == status.HTTP_200_OK
    assert new_surname == response.json()['surname']
# Код состояния - 404
async def test_update_user_http_404_not_found(client):
    user_id = 0
    detail = "Пользователь не найден"
    new_name = "Сергей"
    new_surname = "Смирнов"
    
    user = {
        "item": {
            "name": new_name,
            "surname": new_surname
        }
    }

    response = await client.put(f"/api/users/{user_id}", json=user)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert detail == response.json()['message']
# Код состояния - 422
async def test_update_http_422(client):
    user_id = create_user
    new_name = 123

    user = {
        "item": {
            "name": new_name
        }
    }

    response = await client.put(f"/api/users/{user_id}", json=user)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY