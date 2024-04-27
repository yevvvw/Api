# Нужные библиотеки
import pytest
from httpx import AsyncClient

from models.dbcontext import *
from sqlalchemy import create_engine

import sys
import os

from databases import Database
from main import app

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from public.users import get_database
from config import settings

DATABASE_URL_TEST = settings.POSTGRES_DATABASE_URLT

database_test = Database(DATABASE_URL_TEST)

engine_test = create_engine(DATABASE_URL_TEST, echo=True)

# Создание тестовой таблицы
@pytest.fixture(scope="session", autouse=True)
def create_test_tables():
     Base.metadata.drop_all(bind = engine_test)
     Base.metadata.create_all(bind = engine_test)

@pytest.fixture(scope="session", autouse=True)
def anyio_backend():
    return "asyncio", {"use_uvloop": True}

# Подключение к тестовой БД
def override_get_database():
    database = Database(DATABASE_URL_TEST)
    return database
app.dependency_overrides[get_database] = override_get_database

@pytest.fixture()
def app():
    from main import app
    yield app

@pytest.fixture()
async def client(app):
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client